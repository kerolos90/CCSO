from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, Http404, QueryDict
from .models import *
from .forms import *
# Create your views here.

activity = {
    "Patrol Car": "patrolCar",
    "Patrol Foot": "patrolFoot",
    "Report Writing": "reportWriting",
    "Court": "court",
    "Traffic Detail": "trafficDetail",
    "Special Detail": "specialDetail",
    "Investigate Accident": "investigateAccident",
    "Investigate Criminal": "investigateCriminal",
    "Investigate Other": "investigateOther",
}

productivity = {
    "Arrest Traffic": "arrestTraffic",
    "Arrest Criminal": "arrestCriminal",
    "Written Warnings": "writtenWarnings",
    "Complaints Answered": "complaintsAnswered",
    "Accidents Investigated": "accidentsInvestigated",
    "Vehicles Involved": "vehiclesInvolved",
    "Injuries": "injuries",
    "Fatalities": "fatalities",
    "Papers Served": "papersServed",
}


def ivesdale(request):
    context = {
        "village" : "Ivesdale"
    }
    return render(request, "contract_sheets/contract_base.html", context)


def add_contract_sheet(request):
    date = request.POST.get('date')
    #date = datetime.strptime(date, "%Y-%m-%d").date()

    village = request.POST.get('village')
    context = {
        "date": date,
        "village" : village,
        "ivesdaleForm" : IvesdaleForm(),
        "activity" : activity,
        "productivity" : productivity
    }    
    return render(request, "contract_sheets/partials/add_contract_sheet.html", context)

def save_contract_sheet(request):
    data = QueryDict(request.body).dict()
    return HttpResponse(status=204)
