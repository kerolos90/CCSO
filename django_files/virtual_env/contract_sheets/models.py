from django.db import models
from home.models import Employees

# Create your models here.

EMPLOYEE_CHOICES = []

try:
    for deputies in Employees.objects.order_by('id').values_list('id', 'title', 'l_name'):
        EMPLOYEE_CHOICES.append(
            (f"{deputies[1]} {deputies[2]} #{deputies[0]}", f"{deputies[1]} {deputies[2]} #{deputies[0]}"))
except:
    print("No employees in database")



class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    village = employee = models.CharField(max_length=15)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=False)
    employee = models.CharField(max_length=30, choices=EMPLOYEE_CHOICES)
    carNumber = models.IntegerField()
    start_miles = models.IntegerField()
    end_miles = models.IntegerField()
    total_miles = models.IntegerField()
    start_time = models.TimeField(default='00:00:00')
    end_time = models.TimeField(default='00:00:00')
    total_time = models.IntegerField()
    weather = models.CharField(max_length=10, choices=[(
        'Clear', 'Clear'), ('Rain', 'Rain'), ('Snow', 'Snow')])
    
    patrolCar_timeSpent = models.IntegerField()
    patrolCar_activityLog = models.TextField()
    patrolFoot_timeSpent = models.IntegerField()
    patrolFoot_activityLog = models.TextField()
    reportWriting_timeSpent = models.IntegerField()
    reportWriting_activityLog = models.TextField()
    court_timeSpent = models.IntegerField()
    court_activityLog = models.TextField()
    trafficDetail_timeSpent = models.IntegerField()
    trafficDetail_activityLog = models.TextField()
    specialDetail_timeSpent = models.IntegerField()
    specialDetail_activityLog = models.TextField()
    investigateAccident_timeSpent = models.IntegerField()
    investigateAccident_activityLog = models.TextField()
    investigateCriminal_timeSpent = models.IntegerField()
    investigateCriminal_activityLog = models.TextField()
    investigateOther_timeSpent = models.IntegerField()
    investigateOther_activityLog = models.TextField()

    arrestTraffic_count = models.IntegerField()
    arrestTraffic_activityLog = models.TextField()
    arrestCriminal_count = models.IntegerField()
    arrestCriminal_activityLog = models.TextField()
    writtenWarnings_count = models.IntegerField()
    writtenWarnings_activityLog = models.TextField()
    complaintsAnswered_count = models.IntegerField()
    complaintsAnswered_activityLog = models.TextField()
    accidentsInvestigated_count = models.IntegerField()
    accidentsInvestigated_activityLog = models.TextField()
    vehiclesInvolved_count = models.IntegerField()
    vehiclesInvolved_activityLog = models.TextField()
    injuries_count = models.IntegerField()
    injuries_activityLog = models.TextField()
    fatalities_count = models.IntegerField()
    fatalities_activityLog = models.TextField()
    papersServed_count = models.IntegerField()
    papersServed_activityLog = models.TextField()

    submissionDate = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Ivesdale(BaseModel):
    pass