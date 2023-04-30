from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, Http404, QueryDict
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

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


@login_required(login_url="/login")
def ivesdale(request):
    context = {
        "village" : "Ivesdale",
        "date" : datetime.today().strftime('%Y-%m-%d')
    }
    return render(request, "contract_sheets/contract_base.html", context)


@login_required(login_url="/login")
def philo(request):
    context = {
        "village": "Philo",
        "date": datetime.today().strftime('%Y-%m-%d')
    }
    return render(request, "contract_sheets/contract_base.html", context)


@login_required(login_url="/login")
def savoy(request):
    context = {
        "village": "Savoy",
        "date": datetime.today().strftime('%Y-%m-%d')
    }
    return render(request, "contract_sheets/contract_base.html", context)


@login_required(login_url="/login")
def st_joseph(request):
    context = {
        "village": "St.Joseph",
        "date": datetime.today().strftime('%Y-%m-%d')
    }
    return render(request, "contract_sheets/contract_base.html", context)


@login_required(login_url="/login")
def ivesdale(request):
    context = {
        "village": "Ivesdale",
        "date": datetime.today().strftime('%Y-%m-%d')
    }
    return render(request, "contract_sheets/contract_base.html", context)


@login_required(login_url="/login")
def monthly_totals(request):
    date = request.POST.get('date')
    village = request.POST.get('village')
    totals = ContractSheet.objects.filter(Q(date__startswith=date[:7]) & Q(village=village))
    miles=0
    time_spent=0
    criminal_arrests=0
    traffic_citations=0
    traffic_warnings=0
    papers_served=0
    for contract_sheet in totals:
        miles += contract_sheet.total_miles
        time_spent += contract_sheet.total_time
        criminal_arrests += contract_sheet.arrestCriminal_count
        traffic_citations += contract_sheet.arrestTraffic_count
        traffic_warnings += contract_sheet.writtenWarnings_count
        papers_served += contract_sheet.papersServed_count
    context = {
        "month": datetime.strptime(date, "%Y-%m-%d").strftime("%B"),
        "miles": miles,
        "time_spent" : time_spent,
        "criminal_arrests" : criminal_arrests,
        "traffic_citations" : traffic_citations,
        "traffic_warnings" : traffic_warnings,
        "papers_served" : papers_served
    }
    return render(request, "contract_sheets/partials/monthly_totals.html", context)


@login_required(login_url="/login")
def add_contract_sheet(request):
    date = request.POST.get('date')
    village = request.POST.get('village')
    context = {
        "date": date,
        "village" : village,
        "contract_sheetForm": ContractSheetForm(),
        "activity" : activity,
        "productivity" : productivity
    }    
    return render(request, "contract_sheets/partials/add_contract_sheet.html", context)


@login_required(login_url="/login")
def save_contract_sheet(request):
    form = ContractSheetForm(request.POST)
    if form.is_valid():
        contract_sheet = ContractSheet.objects.get(id=form.save().id)
        contract_sheet.employee=request.user
        contract_sheet.save()
    else:
        print(form.errors)
    return HttpResponse(status=204)


@login_required(login_url="/login")
def contract_sheets_card(request):
    date = request.POST.get('date')
    village = request.POST.get('village')
    context = {
        "date": date,
        "village": village,
        "day_contract_sheets": ContractSheet.objects.filter(Q(date=date) & Q(village=village))
    }
    return render(request, "contract_sheets/partials/contract_sheets_card.html", context)


@login_required(login_url="/login")
def view_contract_sheet(request, village, id):
    context = {
        "contract_sheet": ContractSheet.objects.get(Q(id=id) & Q(village=village)),
        "activity": activity,
        "productivity": productivity
    }
    return render(request, "contract_sheets/partials/view_contract_sheet.html", context)


@login_required(login_url="/login")
def delete_contract_sheet(request, id):
    ContractSheet.objects.get(id=id).delete()
    return HttpResponse(' ')
