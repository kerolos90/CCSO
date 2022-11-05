from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from datetime import date
from home.models import Employees
from .forms import TimeOffRequestForm, EditScheduleForm

# Create your views here.

beats = (
    "Shift Commander #1", "Shift Commander #2", "North (1/2)", "West (3/4)", "Cover (4/5)", "East (5/6)", "South (7/8)"
)
deputies = ("501", "502", "503")

def patrol_schedule(request):
    # try:
    data = Employees.objects.all()
    if request.method == "POST":
        entered_start_date = request.POST['start_date']
        print(entered_start_date)
    form = TimeOffRequestForm()
    editScheduleForm = EditScheduleForm()
    return render(request, "scheduling/patrol_schedule.html", {"form": form, "beats": beats, "deputies": deputies, "editScheduleForm": editScheduleForm})
    # except:
    #      raise Http404()


def investigation_schedule(request):
    return HttpResponse("Investigation schedule")
