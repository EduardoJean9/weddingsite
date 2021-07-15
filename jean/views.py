from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'jean/home.html')

def rsvp(request):
    return render(request,'jean/rsvp.html')

def details(request):
    return render(request,'jean/details.html')

def honeymoon(request):
    return render(request,'jean/honeymoon.html')

def photos(request):
    return render(request,'jean/photos.html')
