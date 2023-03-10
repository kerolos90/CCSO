import datetime
from django.shortcuts import render
from django.http import HttpResponse, Http404, QueryDict
from .models import *
from .forms import *
from .set_date_events import colored_dates

hours = ["first_four", "second_four", "third_four"]
def patrol_beats(date):
    return {
        ShiftCommanderOne.objects.get_or_create(date=date)[0]: "Shift Commander #1",
        ShiftCommanderTwo.objects.get_or_create(date=date)[0]: "Shift Commander #2",
        North.objects.get_or_create(date=date)[0]: "North (1/2)",
        West.objects.get_or_create(date=date)[0]: "West (3/4)",
        Cover.objects.get_or_create(date=date)[0]: "Cover (4/5)",
        East.objects.get_or_create(date=date)[0]: "East (5/6)",
        South.objects.get_or_create(date=date)[0]: "South (7/8)",
    }

def patrol_schedule(request):
   # try:
    current_day = datetime.datetime.now().date()
    context = {
        "hours": hours,
        "current_day": '2023-03-12',
        "colored_dates" : colored_dates,
        "patrol_beats": patrol_beats(current_day)

    }

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        selected_date = request.POST.get('date')
        context["current_day"] = selected_date
        context["patrol_beats"] = patrol_beats(selected_date)
        return render(request, "scheduling/partials/patrol_schedule_partial.html", context)
    return render(request, "scheduling/patrol_schedule.html", context)
    # except:
    #      raise Http404()


def edit_schedule(request):
    date = request.POST.get('date')
    shiftCommanderOneForm = ShiftCommanderOneForm(instance=date)
    shiftCommanderTwoForm = ShiftCommanderTwoForm(instance=date)
    northForm = NorthForm(instance=date)
    westForm = WestForm(instance=date)
    coverForm = CoverForm(instance=date)
    eastForm = EastForm(instance=date)
    southForm = SouthForm(instance=date)

    form_dic = {
        "shiftCommanderOneForm": shiftCommanderOneForm,
        "shiftCommanderTwoForm": shiftCommanderTwoForm,
        "northForm": northForm,
        "westForm": westForm,
        "coverForm": coverForm,
        "eastForm": eastForm,
        "southForm": southForm,

    }

    context = {
        "form_dic": form_dic,
        "date" : date,
        "hours": hours
    }
    return render(request, "scheduling/partials/edit_schedule_partial.html", context)


def patrol_schedule_partial(request):
    test_date = GoldDays.objects.get(date="2023-01-12")
    data = QueryDict(request.body).dict()
    print(data)
    form = EditScheduleForm(data, instance=test_date)
    if form.is_valid():
        form.save()
    context = {
        "test_date": test_date,
        "hours": hours,
    }
    return render(request, "scheduling/partials/patrol_schedule_partial.html", context)
