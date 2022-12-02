from asyncio.windows_events import NULL
from random import choices
from django.db import models
from home.models import Employees
# Create your models here.


EMPLOYEE_CHOICES = [ ("None", "None"),

]
for deputies in Employees.objects.order_by('id').values_list('id', 'title', 'l_name'):
    #deputies = f"{deputies[0]} {deputies[1]} {deputies[2]}"
    EMPLOYEE_CHOICES.append(
        (f"{deputies[1]} {deputies[2]} #{deputies[0]}", str(deputies[0])))


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
        choices=SHORT_DAY_CHOICES
    )
    employee = models.ForeignKey(
        'home.Employees', on_delete=models.CASCADE)


class GoldDays(models.Model):
    date = models.DateField(
        auto_now_add=False, auto_now=False, primary_key=True, blank=False)

    commandOne_first_four = models.CharField(max_length=30,
                                             choices=EMPLOYEE_CHOICES, 
                                             default="None")
    commandOne_second_four = models.CharField(max_length=30,
                                              choices=EMPLOYEE_CHOICES,
                                              default="None")
    commandOne_third_four = models.CharField(max_length=30,
                                             choices=EMPLOYEE_CHOICES,
                                             default="None")

    commandTwo_first_four = models.CharField(max_length=30,
                                             choices=EMPLOYEE_CHOICES,
                                             default="None")
    commandTwo_second_four = models.CharField(max_length=30,
                                              choices=EMPLOYEE_CHOICES,
                                              default="None")
    commandTwo_third_four = models.CharField(max_length=30,
                                             choices=EMPLOYEE_CHOICES,
                                             default="None")

    north_first_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        default="None")
    north_second_four = models.CharField(max_length=30,
                                         choices=EMPLOYEE_CHOICES,
                                         default="None")
    north_third_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        default="None")

    west_first_four = models.CharField(max_length=30,
                                       choices=EMPLOYEE_CHOICES,
                                       default="None")
    west_second_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        default="None")
    west_third_four = models.CharField(max_length=30,
                                       choices=EMPLOYEE_CHOICES,
                                       default="None")

    cover_first_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        default="None")
    cover_second_four = models.CharField(max_length=30,
                                         choices=EMPLOYEE_CHOICES,
                                         default="None")
    cover_third_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        default="None")

    east_first_four = models.CharField(max_length=30,
                                       choices=EMPLOYEE_CHOICES,
                                       default="None")
    east_second_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        default="None")
    east_third_four = models.CharField(max_length=30,
                                       choices=EMPLOYEE_CHOICES,
                                       default="None")

    south_first_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        default="None")
    south_second_four = models.CharField(max_length=30,
                                         choices=EMPLOYEE_CHOICES,
                                         default="None")
    south_third_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        default="None")
