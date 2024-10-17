from django.shortcuts import render, redirect


def home(request):
    return render(request, 'akbar/home.html')

def location(request):
    return render(request, 'akbar/location.html')