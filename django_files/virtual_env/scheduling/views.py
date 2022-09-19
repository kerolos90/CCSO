from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def patrol_schedule(request):
    return HttpResponse("Patrol schedule!")

def investigation_schedule(request):
    return HttpResponse("Investigation schedule")