from scheduling.models import TimeOffRequest

def context_data(request):
    time_off_badge = TimeOffRequest.objects.filter(status="Pending").count()
    can_modify = request.user.groups.filter(name='Employees').exists()
    return {'time_off_badge': time_off_badge, 'can_modify': can_modify}
