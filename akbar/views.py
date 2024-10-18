from django.shortcuts import render, redirect
from .models import DumpStats
from django.contrib.auth import logout
def home(request):
    if request.user.is_authenticated:
        return render(request, 'akbar/dashboard.html', {'username': request.user.username})
    else:
        return render(request, 'akbar/home.html')

def logout_view(request):
    logout(request)
    return render(request, 'akbar/home.html')

def location(request):
    return render(request, 'akbar/location.html')


def map_view(request):
    locations = DumpStats.objects.all()
    return render(request, 'akbar/map.html', {'locations': locations})

def contacts(request):
    return render(request,'akbar/contacts.html')
