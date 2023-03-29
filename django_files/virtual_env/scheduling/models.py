from random import choices
from django.db import models
from home.models import Employees
# Create your models here.


EMPLOYEE_CHOICES = []

try:
    for deputies in Employees.objects.order_by('id').values_list('id', 'title', 'l_name'):
        EMPLOYEE_CHOICES.append(
            (f"{deputies[1]} {deputies[2]} #{deputies[0]}", str(deputies[0])))
except:
    print("No employees in database")

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


class EmpAssignment(models.Model):
    ASSIGNMENT_CHOICES = [
        ("None", "None"),
        ("Gold Days", "Gold Days"),
        ("Gold Nights", "Gold Nights"),
        ("Brown Days", "Brown Days"),
        ("Brown Nights", "Brown Nights"),
        ("St. Joseph", "St. Joseph"),
        ("Savoy", "Savoy"),
        ("Civil Process", "Civil Process"),
        ("Investigations", "Investigations"),
        ("Command Staff", "Command Staff"),
    ]
    SHORT_DAY_CHOICES = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    ]
    assignment = models.CharField(
        max_length=20,
        choices=ASSIGNMENT_CHOICES,
        default="None"
    )
    short_day = models.CharField(
        max_length=20,
        choices=SHORT_DAY_CHOICES,
        blank=True
    )
    employee = models.ForeignKey(
        'home.Employees', on_delete=models.CASCADE)


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
    employee = models.CharField(max_length=30,default='Deputy TEST')
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
    supervisor = models.CharField(max_length=30,default='Sgt. TEST')
    supervisor_comment = models.CharField(max_length=200, blank=True)
    
