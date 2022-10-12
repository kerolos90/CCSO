from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.


def ivesdale(request):
    return render(request, "contract_sheets/ivesdale.html")
