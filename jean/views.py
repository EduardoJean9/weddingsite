from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'jean/home.html',{'nbar': 'home'})

def rsvp(request):
    return render(request,'jean/rsvp.html', {'nbar': 'rsvp'})

def details(request):
    return render(request,'jean/details.html', {'nbar': 'details'})

def honeymoon(request):
    return render(request,'jean/honeymoon.html', {'nbar': 'honeymoon'})

def photos(request):
    return render(request,'jean/photos.html', {'nbar': 'photos'})
