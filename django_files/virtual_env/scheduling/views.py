from django.shortcuts import render
from django.http import HttpResponse, Http404
from datetime import date
# Create your views here.

test_dic = {
    "text": "Patrol challenges",
    "date": date(2015,1,1)

}


def patrol_schedule(request):
    # try:
    return render(request, "scheduling/patrol_schedule.html", {"test_dic": test_dic})
    # except:
    #      raise Http404()


def investigation_schedule(request):
    return HttpResponse("Investigation schedule")


def test(request):
    try:
        return render(request, "scheduling/test.html")
    except:
        raise Http404()
