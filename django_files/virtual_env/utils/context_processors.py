from scheduling.models import TimeOffRequest

def context_data(request):
    time_off_badge = TimeOffRequest.objects.filter(status="Pending").count()
    return {'time_off_badge': time_off_badge}
