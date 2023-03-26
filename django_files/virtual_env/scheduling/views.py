from datetime import datetime
from django.shortcuts import render,redirect
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
        "patrol_beats": patrol_beats(date),
        "savoyOne": SavoyOne.objects.get_or_create(date=date)[0],
        "savoyTwo": SavoyTwo.objects.get_or_create(date=date)[0],
        "savoyThree": SavoyThree.objects.get_or_create(date=date)[0],
        "civilOne": CivilServiceOne.objects.get_or_create(date=date)[0],
        "civilTwo": CivilServiceTwo.objects.get_or_create(date=date)[0],
        "stJoesph": SaintJoseph.objects.get_or_create(date=date)[0],
        "other": Other.objects.filter(date=date),
        "benefit_time": TimeOffRequest.objects.filter(date=date),
        "time_off": TimeOffRequestForm(),
    }

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        selected_date = request.POST.get('date')
        context["date"] = selected_date
        context["patrol_beats"] = patrol_beats(selected_date)
        context["savoyOne"] = SavoyOne.objects.get_or_create(date=selected_date)[0]
        context["savoyTwo"] = SavoyTwo.objects.get_or_create(date=selected_date)[0]
        context["savoyThree"] = SavoyThree.objects.get_or_create(date=selected_date)[0]
        context["civilOne"] = CivilServiceOne.objects.get_or_create(date=selected_date)[0]
        context["civilTwo"] = CivilServiceTwo.objects.get_or_create(date=selected_date)[0]
        context["stJoesph"] = SaintJoseph.objects.get_or_create(date=selected_date)[0]
        context["other"] = Other.objects.filter(date=selected_date)

        return render(request, "scheduling/partials/schedule.html", context)

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
    otherForm  = []
    for instance in Other.objects.filter(date=date):
        form = OtherForm(prefix=instance.id, instance=instance)
        otherForm.append(form)
   
    context = {
        "form_dic": form_dic,
        "date" : date,
        'savoyOneForm': SavoyOneForm(prefix='Savoy1', instance=SavoyOne.objects.get(date=date)),
        'savoyTwoForm': SavoyTwoForm(prefix='Savoy2', instance=SavoyTwo.objects.get(date=date)),
        'savoyThreeForm': SavoyThreeForm(prefix='Savoy3', instance=SavoyThree.objects.get(date=date)),
        'civilOneForm': CivilServiceOneForm(prefix='Civil1', instance=CivilServiceOne.objects.get(date=date)),
        'civilTwoForm': CivilServiceTwoForm(prefix='Civil2', instance=CivilServiceTwo.objects.get(date=date)),
        'stJosephForm': SaintJosephForm(prefix='StJoe', instance=SaintJoseph.objects.get(date=date)),
        'otherForm' : otherForm
    }
    return render(request, "scheduling/partials/edit_schedule.html", context)


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

    SavoyOneForm(data, prefix='Savoy1', instance=SavoyOne.objects.get(date=date)).save()
    SavoyTwoForm(data, prefix='Savoy2',instance=SavoyTwo.objects.get(date=date)).save()
    SavoyThreeForm(data, prefix='Savoy3',instance=SavoyThree.objects.get(date=date)).save()
    CivilServiceOneForm(data, prefix='Civil1',instance=CivilServiceOne.objects.get(date=date)).save()
    CivilServiceTwoForm(data, prefix='Civil2',instance=CivilServiceTwo.objects.get(date=date)).save()
    SaintJosephForm(data, prefix='StJoe', instance=SaintJoseph.objects.get(date=date)).save()

    for instance in Other.objects.filter(date=date):
        form = OtherForm(data, prefix=instance.id, instance=instance)
        form.save()



    context = {
        "patrol_beats": patrol_beats(date),
        "hours": hours,
        "date": date,
        "savoyOne": SavoyOne.objects.get_or_create(date=date)[0],
        "savoyTwo": SavoyTwo.objects.get_or_create(date=date)[0],
        "savoyThree": SavoyThree.objects.get_or_create(date=date)[0],
        "civilOne": CivilServiceOne.objects.get_or_create(date=date)[0],
        "civilTwo": CivilServiceTwo.objects.get_or_create(date=date)[0],
        "stJoesph": SaintJoseph.objects.get_or_create(date=date)[0],
        "other": Other.objects.filter(date=date),
        "time_off": TimeOffRequestForm()
    }
    return render(request, "scheduling/partials/schedule.html", context)

def delete_other_row(request):
    id = list(QueryDict(request.body).keys())
    Other.objects.get(id=id[0]).delete()
    return HttpResponse('')

def add_other_row(request):
    Other(date=request.POST.get('date')).save()
    return edit_schedule(request)

def time_off_request(request):
    data = QueryDict(request.body).dict()
    TimeOffRequest(**data).save()
    return HttpResponse(status=204)

def benefit_time_table(request):
    context = {
        "benefit_time": TimeOffRequest.objects.filter(date=request.POST.get('date')),
        "date": request.POST.get('date')
    }    
    return render(request, "scheduling/partials/benefit_time_partial.html",context)

def benefit_time_review(request):
    id = list(QueryDict(request.body).keys())
    time_off_request = TimeOffRequest.objects.get(id=id[0])
    time_off_review = SupervisorTimeOffReview(instance=time_off_request)
    context = {
        "time_off_request": time_off_request,
        "time_off_review" : time_off_review
    }
    return render(request, "scheduling/partials/benefit_time_review_partial.html", context)













