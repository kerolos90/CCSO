from datetime import datetime, date
from django.shortcuts import render
from django.http import HttpResponse, Http404, QueryDict
from .models import *
from .forms import *
from .set_date_events import colored_dates
from django.contrib.auth.decorators import login_required
from django.db.models import Q

benefit_type = ['vacation', 'comp', 'holiday', 'sick', 'personal']


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


@login_required(login_url="login")
def patrol_schedule(request):
   # try:
    date = datetime.today().strftime('%Y-%m-%d')
    context = {
        "date": date,
        "colored_dates": colored_dates,
    }

    return render(request, "scheduling/patrol_schedule.html", context)
    # except:
    #      raise Http404()


@login_required(login_url="login")
def edit_schedule(request):
    date = request.POST.get('date')
    shiftCommanderOneForm = ShiftCommanderOneForm(
        prefix='SC1', instance=ShiftCommanderOne.objects.get(date=date))
    shiftCommanderTwoForm = ShiftCommanderTwoForm(
        prefix='SC2', instance=ShiftCommanderTwo.objects.get(date=date))
    northForm = NorthForm(
        prefix='North', instance=North.objects.get(date=date))
    westForm = WestForm(prefix='West', instance=West.objects.get(date=date))
    coverForm = CoverForm(
        prefix='Cover', instance=Cover.objects.get(date=date))
    eastForm = EastForm(prefix='East', instance=East.objects.get(date=date))
    southForm = SouthForm(
        prefix='South', instance=South.objects.get(date=date))

    form_dic = {
        shiftCommanderOneForm: "Shift Commander #1",
        shiftCommanderTwoForm: "Shift Commander #2",
        northForm: "North (1/2)",
        westForm: "West (3/4)",
        coverForm: "Cover (4/5)",
        eastForm: "East (5/6)",
        southForm: "South (7/8)"
    }
    otherForm = []
    for instance in Other.objects.filter(date=date):
        form = OtherForm(prefix=instance.id, instance=instance)
        otherForm.append(form)

    context = {
        "form_dic": form_dic,
        "date": date,
        'savoyOneForm': SavoyOneForm(prefix='Savoy1', instance=SavoyOne.objects.get(date=date)),
        'savoyTwoForm': SavoyTwoForm(prefix='Savoy2', instance=SavoyTwo.objects.get(date=date)),
        'savoyThreeForm': SavoyThreeForm(prefix='Savoy3', instance=SavoyThree.objects.get(date=date)),
        'civilOneForm': CivilServiceOneForm(prefix='Civil1', instance=CivilServiceOne.objects.get(date=date)),
        'civilTwoForm': CivilServiceTwoForm(prefix='Civil2', instance=CivilServiceTwo.objects.get(date=date)),
        'stJosephForm': SaintJosephForm(prefix='StJoe', instance=SaintJoseph.objects.get(date=date)),
        'otherForm': otherForm
    }
    return render(request, "scheduling/partials/edit_schedule.html", context)


@login_required(login_url="login")
def patrol_schedule_partial(request):
    if request.method == 'GET':
        date = request.GET.get('date')
        context = {
            "patrol_beats": patrol_beats(date),
            "date": date,
            "savoyOne": SavoyOne.objects.get_or_create(date=date)[0],
            "savoyTwo": SavoyTwo.objects.get_or_create(date=date)[0],
            "savoyThree": SavoyThree.objects.get_or_create(date=date)[0],
            "civilOne": CivilServiceOne.objects.get_or_create(date=date)[0],
            "civilTwo": CivilServiceTwo.objects.get_or_create(date=date)[0],
            "stJoesph": SaintJoseph.objects.get_or_create(date=date)[0],
            "other": Other.objects.filter(date=date),
            "time_off": TimeOffRequestForm(),
            "benefit_type": benefit_type,
            "can_modify": request.user.groups.filter(name='Employees').exists(),
            "colored_dates": colored_dates,
        }
        return render(request, "scheduling/partials/schedule.html", context)

    date = request.POST.get('date')
    data = QueryDict(request.body).dict()

    ShiftCommanderOneForm(data, instance=ShiftCommanderOne.objects.get(
        date=date), prefix="SC1").save()
    ShiftCommanderTwoForm(data, instance=ShiftCommanderTwo.objects.get(
        date=date), prefix="SC2").save()
    NorthForm(data, instance=North.objects.get(
        date=date), prefix="North").save()
    WestForm(data, instance=West.objects.get(date=date), prefix="West").save()
    CoverForm(data, instance=Cover.objects.get(
        date=date), prefix="Cover").save()
    EastForm(data, instance=East.objects.get(date=date), prefix="East").save()
    SouthForm(data, instance=South.objects.get(
        date=date), prefix="South").save()

    SavoyOneForm(data, prefix='Savoy1',
                 instance=SavoyOne.objects.get(date=date)).save()
    SavoyTwoForm(data, prefix='Savoy2',
                 instance=SavoyTwo.objects.get(date=date)).save()
    SavoyThreeForm(data, prefix='Savoy3',
                   instance=SavoyThree.objects.get(date=date)).save()
    CivilServiceOneForm(data, prefix='Civil1',
                        instance=CivilServiceOne.objects.get(date=date)).save()
    CivilServiceTwoForm(data, prefix='Civil2',
                        instance=CivilServiceTwo.objects.get(date=date)).save()
    SaintJosephForm(data, prefix='StJoe',
                    instance=SaintJoseph.objects.get(date=date)).save()

    for instance in Other.objects.filter(date=date):
        form = OtherForm(data, prefix=instance.id, instance=instance)
        form.save()

    context = {
        "patrol_beats": patrol_beats(date),
        "date": date,
        "savoyOne": SavoyOne.objects.get_or_create(date=date)[0],
        "savoyTwo": SavoyTwo.objects.get_or_create(date=date)[0],
        "savoyThree": SavoyThree.objects.get_or_create(date=date)[0],
        "civilOne": CivilServiceOne.objects.get_or_create(date=date)[0],
        "civilTwo": CivilServiceTwo.objects.get_or_create(date=date)[0],
        "stJoesph": SaintJoseph.objects.get_or_create(date=date)[0],
        "other": Other.objects.filter(date=date),
        "time_off": TimeOffRequestForm(),
        "benefit_type": benefit_type,
        "can_modify": request.user.groups.filter(name='Employees').exists(),
        "colored_dates": colored_dates,
    }
    return render(request, "scheduling/partials/schedule.html", context)


@login_required(login_url="login")
def delete_other_row(request, id):
    Other.objects.get(id=id).delete()
    return HttpResponse('')


@login_required(login_url="login")
def add_other_row(request):
    Other(date=request.POST.get('date')).save()
    return edit_schedule(request)


@login_required(login_url="login")
def time_off_request(request):
    data = QueryDict(request.body).dict()
    TimeOffRequest(employee=request.user, **data).save()
    return HttpResponse(status=204)


@login_required(login_url="login")
def benefit_time_table(request):
    date = request.POST.get('date')
    context = {
        "benefit_time": TimeOffRequest.objects.filter(date__startswith=date),
        "date": date,
    }
    return render(request, "scheduling/partials/benefit_time_partial.html", context)


@login_required(login_url="login")
def benefit_time_review(request, id=None):
    if request.method == 'POST':
        time_off_request = TimeOffRequest.objects.get(
            id=request.POST.get('id'))
        time_off_request.status = request.POST.get('status')
        time_off_request.supervisor_comment = request.POST.get(
            'supervisor_comment')
        time_off_request.supervisor = request.POST.get('supervisor')

        time_off_request.save()
        return HttpResponse(status=204)

    time_off_request = TimeOffRequest.objects.get(id=id)
    time_off_review = SupervisorTimeOffReviewForm(instance=time_off_request)
    context = {
        "time_off_request": time_off_request,
        "time_off_review": time_off_review,
        "benefit_type": benefit_type
    }

    return render(request, "scheduling/partials/benefit_time_review_partial.html", context)

@login_required(login_url="login")
def benefit_requests(request):
    month_year = (date.today().strftime('%Y-%m'))
    context = {
        "month_year": month_year,
        "benefit_time": TimeOffRequest.objects.filter(date__startswith=month_year)
    }
    return render(request, "scheduling/benefit_requests.html", context)

@login_required(login_url="login")
def my_benefit_requests(request):
    month_year = (date.today().strftime('%Y-%m'))
    context = {
        "month_year": month_year,
        "benefit_time": TimeOffRequest.objects.filter(Q(date__startswith=month_year) & Q(employee=request.user))
    }
    return render(request, "scheduling/my_benefit_requests.html", context)

@login_required(login_url="login")
def my_benefit_time_table(request):
    date = request.POST.get('date')
    context = {
        "benefit_time": TimeOffRequest.objects.filter(Q(date__startswith=date) & Q(employee=request.user)),
        "date": date,
        "benefit_type": benefit_type,
    }
    return render(request, "scheduling/partials/my_benefit_time_view_partial.html", context)

@login_required(login_url="/login")
def delete_my_request(request, id):
    TimeOffRequest.objects.get(id=id).delete()
    return HttpResponse('')
