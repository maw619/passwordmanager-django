from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from dash.models import PasswordEntry, User
from dash.forms import AddForm
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.contrib import messages
from django.db.models import Q

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import ipinfo
from django.contrib.messages import SUCCESS

def get_client_ip(request):
    """Retrieves the client's IP address from request headers."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # Get the first IP in case of multiple
    else:
        ip = request.META.get('REMOTE_ADDR')  # Fallback if no proxy is used
    return ip

def get_ip_details(ip_address):
    """Fetches IP geolocation details from ipinfo.io."""
    ipinfo_token = getattr(settings, "IPINFO_TOKEN", None) 
    handler = ipinfo.getHandler(ipinfo_token)
    ip_data = handler.getDetails(ip_address)
    
    return ip_data.all  # Convert to dictionary

def location(request):
    """Dynamically fetches the visitor's IP and retrieves location details."""
    user_ip = get_client_ip(request)  # Get user's IP dynamically
    ip_data = get_ip_details(user_ip)  # Fetch IP details

    response_string = 'The IP address {} is located at the coordinates {}, which is in the city {}.'.format(
        ip_data.get('ip', 'Unknown'), ip_data.get('loc', 'Unknown'), ip_data.get('city', 'Unknown')
    )

    print(response_string)  # For debugging/logging
    messages.success(request, response_string)

@login_required
def index(request):  
    location(request)
    # print(get_client_ip(request)) 
    id = request.user.id
    passes = PasswordEntry.objects.filter(user=id)
    context = {
        "ip":location(request),
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