from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from dash.models import PasswordEntry, User
from dash.forms import AddForm
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.contrib import messages
from django.db.models import Q
import ipaddress

def get_ipv4_from_x_forwarded_for(x_forwarded_for):
    """Extracts and prioritizes IPv4 from a comma-separated list of IPs."""
    if not x_forwarded_for:
        return None
    
    for ip in x_forwarded_for.split(','):
        ip = ip.strip()
        if isinstance(ipaddress.ip_address(ip), ipaddress.IPv4Address):
            return ip  # Return the first IPv4 address found
    return None  # No IPv4 found

def get_client_ipv4(request):
    """Fetches the IPv4 address of the client if available."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    
    ip = get_ipv4_from_x_forwarded_for(x_forwarded_for)
    if ip:
        return ip  # Return IPv4 if found

    # Fallback to REMOTE_ADDR if no IPv4 found in X-Forwarded-For
    remote_ip = request.META.get('REMOTE_ADDR')
    if remote_ip and isinstance(ipaddress.ip_address(remote_ip), ipaddress.IPv4Address):
        return remote_ip

    return None  # No IPv4 available
 

 

@login_required
def index(request):  
    print(get_client_ipv4(request)) 
    id = request.user.id
    passes = PasswordEntry.objects.filter(user=id)
    context = {
        "passes":passes, 
    } 
    return render(request, 'index.html', context)

@login_required
def search(request): 
    q = request.GET.get('q').strip()
    if q:
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