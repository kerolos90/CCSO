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
    patrolFoot_activityLog = models.CharField(max_length=200)
    reportWriting_timeSpent = models.IntegerField()
    reportWriting_activityLog = models.CharField(max_length=200)
    court_timeSpent = models.IntegerField()
    court_activityLog = models.CharField(max_length=200)
    trafficDetail_timeSpent = models.IntegerField()
    trafficDetail_activityLog = models.CharField(max_length=200)
    specialDetail_timeSpent = models.IntegerField()
    specialDetail_activityLog = models.CharField(max_length=200)
    investigateAccident_timeSpent = models.IntegerField()
    investigateAccident_activityLog = models.CharField(max_length=200)
    investigateCriminal_timeSpent = models.IntegerField()
    investigateCriminal_activityLog = models.CharField(max_length=200)
    investigateOther_timeSpent = models.IntegerField()
    investigateOther_activityLog = models.CharField(max_length=200)
    total_timeSpent = models.IntegerField()

    arrestTraffic_count = models.IntegerField()
    arrestTraffic_activityLog = models.TextField()
    arrestCriminal_count = models.IntegerField()
    arrestCriminal_activityLog = models.CharField(max_length=10, default=0)
    writtenWarnings_count = models.IntegerField()
    writtenWarnings_activityLog = models.CharField(max_length=10, default=0)
    complaintsAnswered_count = models.IntegerField()
    complaintsAnswered_activityLog = models.CharField(max_length=10, default=0)
    accidentsInvestigated_count = models.IntegerField()
    accidentsInvestigated_activityLog = models.CharField(max_length=10, default=0)
    vehiclesInvolved_count = models.IntegerField()
    injuries_count = models.IntegerField()
    fatalities_count = models.IntegerField()
    papersServed_count = models.IntegerField()
    papersServed_activityLog = models.CharField(max_length=10, default=0)

    submissionDate = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Ivesdale(BaseModel):
    pass