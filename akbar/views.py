from django.shortcuts import render, redirect
from .models import DumpStats

def home(request):
    return render(request, 'akbar/home.html')

def location(request):
    return render(request, 'akbar/location.html')


def map_view(request):
    locations = DumpStats.objects.all()
    return render(request, 'akbar/map.html', {'locations': locations})
