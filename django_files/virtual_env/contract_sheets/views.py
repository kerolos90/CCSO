from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.


def ivesdale(request):
    context = {
        "village" : "Ivesdale"
    }
    return render(request, "contract_sheets/contract_base.html", context)


def add_contract_sheet(request):
    return render(request, "contract_sheets/partials/add_contract_sheet.html")
