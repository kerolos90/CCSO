from django.db import models
from home.models import Employees
# Create your models here.

class Patrol_Teams(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    team = models.CharField(max_length=20, blank=True)
    short_day = models.CharField(max_length=20, blank=True)
