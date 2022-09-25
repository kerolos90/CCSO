from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.

test_dic = {
    "text": "Patrol challenges",
    'range': range(10)

}
def patrol_schedule(request):
    try:
        return render(request,"scheduling/patrol_schedule.html", test_dic)
    except:
         raise Http404()


def investigation_schedule(request):
    return HttpResponse("Investigation schedule")
