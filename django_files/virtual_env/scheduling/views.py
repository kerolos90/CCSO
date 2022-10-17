from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from datetime import date
from home.models import Employees

# Create your views here.

test_dic = {
    "text": "Patrol challenges",
    "date": date(2015,1,1)

}


def patrol_schedule(request):
    # try:
    data = Employees.objects.all()

    return render(request, "scheduling/patrol_schedule.html", {"data": data})
    # except:
    #      raise Http404()


def investigation_schedule(request):
    return HttpResponse("Investigation schedule")
