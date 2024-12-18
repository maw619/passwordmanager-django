from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from dash.models import PasswordEntry, User
from dash.forms import AddForm
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.contrib import messages
from django.db.models import Q


@login_required
def index(request):  
    # q = request.GET.get('q')
    # if q is not None:
    #     vector = SearchVector('site_name','site_url','username','encrypted_password','remarks')
    #     query = SearchQuery(q)
    #     passes = PasswordEntry.objects.annotate(search=vector).filter(search=query) 
    #     if q is not None and passes.count() == 0:
    #         messages.warning(request, "no results found") 
    # else:
    #     id = request.user.id
    #     passes = PasswordEntry.objects.filter(user=id) 
    id = request.user.id
    passes = PasswordEntry.objects.filter(user=id)
    context = {
        "passes":passes,
        # "word":q
    } 
    return render(request, 'index.html', context)

@login_required
def search(request):
 
    q = request.GET.get('q') 
    if q is not None:
        passes = PasswordEntry.objects.filter(Q(site_name__icontains=q) | Q(site_url__icontains=q) | Q(encrypted_password__icontains=q) | Q(remarks__icontains=q))
    if q is None or q == "":
        id = request.user.id
        passes = PasswordEntry.objects.filter(user=id) 
    return render(request, 'partials/results.html', {"passes":passes})

@login_required
def add_record(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            # Save the form but don't commit to the database yet
            new_record = form.save(commit=False)
            # Assign the logged-in user to the record
            new_record.user = request.user
            new_record.save()
            return redirect("index")
    else:
        form = AddForm()
    return render(request, "add-record.html", {"form": form})

@login_required
def update_record(request, pk):
    pass_by_id = PasswordEntry.objects.get(id=pk)
    form = AddForm(instance=pass_by_id)
    print(pass_by_id)
    if request.method == "POST":
        form = AddForm(request.POST or None, instance=pass_by_id)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'update-record.html', {'form':form})
    
@login_required
def delete_record(request, pk):
    delete_pass_by_id = PasswordEntry.objects.get(id=pk)
    delete_pass_by_id.delete()
    return redirect("index")
  
def logout_user(request):
    logout(request)