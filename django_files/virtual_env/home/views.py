from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.

def home(request):
    return render(request, "home/index.html")

def login(request):
    return render(request, "home/login.html")