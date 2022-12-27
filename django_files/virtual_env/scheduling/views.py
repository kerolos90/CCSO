from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from datetime import date
from home.models import Employees
from .models import GoldDays
from .forms import TimeOffRequestForm, EditScheduleForm

# Create your views here.

beats = {
    "commandOne": "Shift Commander #1",
    "commandTwo": "Shift Commander #2",
    "north": "North (1/2)",
    "west": "West (3/4)",
    "cover": "Cover (4/5)",
    "east": "East (5/6)", 
    "south": "South (7/8)",
}

hours = ["_first_four", "_second_four", "_third_four"]


def patrol_schedule(request):
     #try:
    test_date = GoldDays.objects.get(date="2022-11-10")
    form = TimeOffRequestForm()
    context = {
        "test_date": test_date,
        "form": form,
        "beats": beats,
        "hours": hours        
    }
    return render(request, "scheduling/patrol_schedule.html", context)
    # except:
    #      raise Http404()

def edit_schedule(request, selected_beat):
    test_date = GoldDays.objects.get(date="2022-11-10")
    editScheduleForm = EditScheduleForm(request.POST, instance=test_date)
    beat = beats[selected_beat]
    fields_to_edit = []
    for section in hours :
        fields_to_edit.append(editScheduleForm[selected_beat + section])
    context = {
        "beat": beat,
        "test_date": test_date,
        "selected_beat": selected_beat,
        "editScheduleForm": editScheduleForm,
        "fields_to_edit": fields_to_edit,        
    }
    return render(request, "scheduling/partials/edit_schedule_partial.html", context)

def patrol_schedule_partial(request, selected_beat):
    test_date = GoldDays.objects.get(date="2022-11-10")
    beat = beats[selected_beat]
    fields_to_show = []
    for section in hours:
        attr = selected_beat+section
        fields_to_show.append(test_date)
    context = {
        "fields_to_show": fields_to_show,
        "selected_beat":selected_beat,
        "test_date": vars(test_date),
        "beat": beat,
    }

    return render(request, "scheduling/partials/patrol_schedule_partial.html", context)
