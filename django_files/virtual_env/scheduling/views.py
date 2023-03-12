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
        "current_day": current_day,
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
    shiftCommanderOneForm = ShiftCommanderOneForm(instance=ShiftCommanderOne.objects.get(date=date))
    shiftCommanderTwoForm = ShiftCommanderTwoForm(instance=ShiftCommanderTwo.objects.get(date=date))
    northForm = NorthForm(instance=North.objects.get(date=date))
    westForm = WestForm(instance=West.objects.get(date=date))
    coverForm = CoverForm(instance=Cover.objects.get(date=date))
    eastForm = EastForm(instance=East.objects.get(date=date))
    southForm = SouthForm(instance=South.objects.get(date=date))

    form_dic = {
        shiftCommanderOneForm : "Shift Commander #1",
        shiftCommanderTwoForm: "Shift Commander #2",
        northForm: "North (1/2)",
        westForm: "West (3/4)",
        coverForm: "Cover (4/5)",
        eastForm: "East (5/6)",
        southForm: "South (7/8)"
    }

    context = {
        "form_dic": form_dic,
        "date" : date,
    }
    return render(request, "scheduling/partials/edit_schedule_partial.html", context)


def patrol_schedule_partial(request):
    date = request.POST.get('date')
    form_list =[
        ShiftCommanderOneForm(instance=ShiftCommanderOne.objects.get(date=date)),
        ShiftCommanderTwoForm(instance=ShiftCommanderTwo.objects.get(date=date)),
        NorthForm(instance=North.objects.get(date=date)),
        WestForm(instance=West.objects.get(date=date)),
        CoverForm(instance=Cover.objects.get(date=date)),
        EastForm(instance=East.objects.get(date=date)),
        SouthForm(instance=South.objects.get(date=date))
    ]

    # test_date = GoldDays.objects.get(date="2023-01-12")
    data = QueryDict(request.body).dict()
    print(data)
    # form = EditScheduleForm(data, instance=test_date)
    # if form.is_valid():
    #     form.save()
    context = {
        # "test_date": test_date,
        "hours": hours,
    }
    return render(request, "scheduling/partials/patrol_schedule_partial.html", context)
