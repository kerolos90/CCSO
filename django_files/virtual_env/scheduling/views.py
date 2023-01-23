import datetime
from django.shortcuts import render
from django.http import HttpResponse, Http404, QueryDict
from .models import GoldDays
from .forms import TimeOffRequestForm, EditScheduleForm
from .set_date_events import colored_dates


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
#      #try:
    current_day = datetime.datetime.now().date()
    form = TimeOffRequestForm()
    context = {
        "test_date": GoldDays.objects.get(date='2023-01-12'),
        "form": form,
        "beats": beats,
        "hours": hours,
        "current_day": current_day.strftime("%B %d, %Y"),
        "colored_dates" : colored_dates

    }
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.headers.get('HX-Request'):
        context["test_date"] = GoldDays.objects.get(date="2023-01-13")
        # current_day = request.session['date']
        print(request.POST.get('date'))
    
        return render(request, "scheduling/partials/load_full_schedule_partial.html", context)
    return render(request, "scheduling/patrol_schedule.html", context)
    # except:
    #      raise Http404()


def edit_schedule(request):
    test_date = GoldDays.objects.get(date="2023-01-12")
    editScheduleForm = EditScheduleForm(instance=test_date)
    context = {
        "beats": beats,
        "editScheduleForm": editScheduleForm,
        "hours": hours,
    }
    print(request.POST)

    return render(request, "scheduling/partials/edit_schedule_partial.html", context)


def patrol_schedule_partial(request):
    test_date = GoldDays.objects.get(date="2023-01-12")
    data = QueryDict(request.body).dict()
    form = EditScheduleForm(data, instance=test_date)
    print(data)

    if form.is_valid():
        form.save()

    context = {
        "test_date": test_date,
        "beats": beats,
        "hours": hours
    }

    return render(request, "scheduling/partials/patrol_schedule_partial.html", context)

# def edit_schedule(request, selected_beat):
#     test_date = GoldDays.objects.get(date="2023-01-12")
#     editScheduleForm = EditScheduleForm(instance=test_date)
#     beat = beats[selected_beat]
#     fields_to_edit = []
#     for section in hours :
#         fields_to_edit.append(editScheduleForm[selected_beat + section])
    
#     context = {
#         "beat": beat,
#         "test_date": test_date,
#         "selected_beat": selected_beat,
#         "editScheduleForm": editScheduleForm,
#         "fields_to_edit": fields_to_edit,        
#     }
#     return render(request, "scheduling/partials/edit_schedule_partial.html", context)



# def patrol_schedule_partial(request, selected_beat):
#     test_date = GoldDays.objects.get(date="2023-01-12")
#     beat = beats[selected_beat]
#     data = QueryDict(request.body).dict()
#     form = EditScheduleForm(data,instance=test_date)
#     print(form)

#     context = {
#         "selected_beat":selected_beat,
#         "test_date": test_date,
#         "beat": beat,
#         "hours": hours        
#     }
#     if form.is_valid():
#         form.save()
#     return render(request, "scheduling/partials/patrol_schedule_partial.html", context)