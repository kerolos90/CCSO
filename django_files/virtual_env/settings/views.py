from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.


def settings(request):
    return render(request,"settings/settings.html")
