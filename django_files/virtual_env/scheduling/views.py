from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from datetime import date
from home.models import Employees
from .models import GoldDays
from .forms import TimeOffRequestForm, EditScheduleForm

# Create your views here.

beats = {
    "Shift Commander #1": "commandOne",
    "Shift Commander #2": "commandtwo",
    "North (1/2)": "north",
    "West (3/4)": "west",
    "Cover (4/5)": "cover",
    "East (5/6)": "east", 
    "South (7/8)": "south"
}
beat_sections = (
    "commandOne", "commandTwo", "north", "west", "cover", "east", "south"
)
deputies = ("501", "502", "503")


def patrol_schedule(request):
    # try:
    test_date = GoldDays.objects.get(date="2022-11-10")
    if request.method == "POST":
        editForm = EditScheduleForm(request.POST, instance=test_date)
        if editForm.is_valid():
            editForm.save()
            entered_start_date = request.POST.get('commandOne_first_four', False)
            print(entered_start_date)

    form = TimeOffRequestForm()
    editScheduleForm = EditScheduleForm()
    return render(request, "scheduling/patrol_schedule.html", {
        "form": form,
        "beats": beats,
        "deputies": deputies,
        "editScheduleForm": editScheduleForm,
        "beat_sections": beat_sections,
    })
    # except:
    #      raise Http404()


def investigation_schedule(request):
    return HttpResponse("Investigation schedule")
