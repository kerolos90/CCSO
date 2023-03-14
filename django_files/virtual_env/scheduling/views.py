from datetime import datetime
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
    date = datetime.today().strftime('%Y-%m-%d')
    context = {
        "hours": hours,
        "date": date,
        "colored_dates" : colored_dates,
        "patrol_beats": patrol_beats(date)
    }
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        selected_date = request.POST.get('date')
        context["date"] = selected_date
        context["patrol_beats"] = patrol_beats(selected_date)
        return render(request, "scheduling/partials/patrol_schedule_partial.html", context)

    return render(request, "scheduling/patrol_schedule.html", context)
    # except:
    #      raise Http404()



def edit_schedule(request):
    date = request.POST.get('date')

    shiftCommanderOneForm = ShiftCommanderOneForm(prefix='SC1',instance=ShiftCommanderOne.objects.get(date=date))
    shiftCommanderTwoForm = ShiftCommanderTwoForm(prefix='SC2',instance=ShiftCommanderTwo.objects.get(date=date))
    northForm = NorthForm(prefix='North', instance=North.objects.get(date=date))
    westForm = WestForm(prefix='West', instance=West.objects.get(date=date))
    coverForm = CoverForm(prefix='Cover', instance=Cover.objects.get(date=date))
    eastForm = EastForm(prefix='East', instance=East.objects.get(date=date))
    southForm = SouthForm(prefix='South', instance=South.objects.get(date=date))

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
    data = QueryDict(request.body).dict()

    ShiftCommanderOneForm(data, instance=ShiftCommanderOne.objects.get(date=date), prefix="SC1").save()
    ShiftCommanderTwoForm(data, instance=ShiftCommanderTwo.objects.get(date=date), prefix="SC2").save()
    NorthForm(data, instance=North.objects.get(date=date), prefix="North").save()
    WestForm(data, instance=West.objects.get(date=date), prefix="West").save()
    CoverForm(data, instance=Cover.objects.get(date=date), prefix="Cover").save()
    EastForm(data, instance=East.objects.get(date=date), prefix="East").save()
    SouthForm(data, instance=South.objects.get(date=date), prefix="South").save()

    context = {
        "patrol_beats": patrol_beats(date),
        "hours": hours,
        "date": date
    }
    return render(request, "scheduling/partials/patrol_schedule_partial.html", context)

