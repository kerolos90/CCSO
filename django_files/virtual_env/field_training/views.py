from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.


def field_training(request):
    return render(request, "field_training/recruits.html")