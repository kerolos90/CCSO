from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="login")
def home(request):
    return render(request, "home/index.html")


@login_required(login_url="login")
def forms(request):
    return render(request, "home/forms.html")


@login_required(login_url="login")
def ehd(request):
    return render(request, "home/ehd.html")

@login_required(login_url="login")
def employee_assignments(request):
    return render(request, "home/employee_assignments.html")
