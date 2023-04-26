from django.db import models
from home.models import EMPLOYEE_CHOICES
from django.conf import settings  

# Create your models here.


ACTIVITY_CHOICES = [
    ("North (1/2)", "North (1/2)"),
    ("West (3/4)", "West (3/4)"),
    ("Cover (4/5)", "Cover (4/5)"),
    ("East (5/6)", "East (5/6)"),
    ("South (7/8)", "South (7/8)"),
    ("Savoy (10)", "South (10)"),
    ("St. Joseph (11)", "St. Joseph (11)"),
    ("Field Training (FTO)", "Field Training (FTO)"),
    ("Training", "Training"),
    ("Recruit", "Recruit")
]

class ShiftCommanderOne(models.Model):
    date = models.DateField(
        auto_now_add=False, auto_now=False, primary_key=True, blank=False)
    first_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    second_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    third_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    fourth_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    fifth_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    sixth_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)


class ShiftCommanderTwo(models.Model):
    date = models.DateField(
        auto_now_add=False, auto_now=False, primary_key=True, blank=False)
    first_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    second_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    third_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    fourth_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    fifth_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    sixth_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)


class North(models.Model):
    date = models.DateField(
        auto_now_add=False, auto_now=False, primary_key=True, blank=False)
    first_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    second_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    third_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    fourth_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    fifth_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    sixth_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)


class West(models.Model):
    date = models.DateField(
        auto_now_add=False, auto_now=False, primary_key=True, blank=False)
    first_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    second_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    third_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    fourth_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    fifth_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    sixth_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)


class East(models.Model):
    date = models.DateField(
        auto_now_add=False, auto_now=False, primary_key=True, blank=False)
    first_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    second_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    third_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    fourth_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    fifth_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    sixth_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)


class Cover(models.Model):
    date = models.DateField(
        auto_now_add=False, auto_now=False, primary_key=True, blank=False)
    first_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    second_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    third_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    fourth_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    fifth_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    sixth_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)


class South(models.Model):
    date = models.DateField(
        auto_now_add=False, auto_now=False, primary_key=True, blank=False)
    first_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    second_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    third_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    fourth_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    fifth_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    sixth_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)


class SaintJoseph(models.Model):
    date = models.DateField(
        auto_now_add=False, auto_now=False, primary_key=True, blank=False)
    first_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    second_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)


class SavoyOne(models.Model):
    date = models.DateField(
        auto_now_add=False, auto_now=False, primary_key=True, blank=False)
    first_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    second_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)


class SavoyTwo(models.Model):
    date = models.DateField(
        auto_now_add=False, auto_now=False, primary_key=True, blank=False)
    first_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    second_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)


class SavoyThree(models.Model):
    date = models.DateField(
        auto_now_add=False, auto_now=False, primary_key=True, blank=False)
    first_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    second_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)


class CivilServiceOne(models.Model):
    date = models.DateField(
        auto_now_add=False, auto_now=False, primary_key=True, blank=False)
    first_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    second_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)


class CivilServiceTwo(models.Model):
    date = models.DateField(
        auto_now_add=False, auto_now=False, primary_key=True, blank=False)
    first_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    second_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)

class Other(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(
        auto_now_add=False, auto_now=False, blank=False)
    beat_assignment = models.CharField(
        max_length=30, choices=ACTIVITY_CHOICES, blank=True)
    employee = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    start_time = models.TimeField(
        auto_now=False, auto_now_add=False, default='06:00:00')
    end_time = models.TimeField(
        auto_now=False, auto_now_add=False, default='06:00:00')
    comment = models.CharField(max_length=200, blank=True)

class TimeOffRequest(models.Model):
    date = models.DateField(auto_now_add=False, auto_now=False, blank=False)
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_time = models.TimeField(default='00:00:00')
    end_time = models.TimeField(default='00:00:00')
    comment = models.CharField(max_length=200, blank=True)
    vacation = models.CharField(max_length=10,default=0)
    comp = models.CharField(max_length=10, default=0)
    holiday = models.CharField(max_length=10, default=0)
    sick = models.CharField(max_length=10, default=0)
    personal = models.CharField(max_length=10, default=0)
    submitted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[(
        'Approved', 'Approved'), ('Denied', 'Denied'), ('Pending', 'Pending')], default="Pending")
    reviewed = models.DateTimeField(auto_now=True)
    supervisor = models.CharField(max_length=30)
    supervisor_comment = models.CharField(max_length=200, blank=True)
    
