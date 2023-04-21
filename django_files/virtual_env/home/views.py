from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/login")
def home(request):
    return render(request, "home/index.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        return redirect('login_user')
    else: 
        return render(request, "registration/login.html")