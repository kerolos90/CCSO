from random import choices
from django.db import models
from home.models import Employees
# Create your models here.


EMPLOYEE_CHOICES = [('None', 'None'),

                    ]
try:
    for deputies in Employees.objects.order_by('id').values_list('id', 'title', 'l_name'):
        EMPLOYEE_CHOICES.append(
            (f"{deputies[1]} {deputies[2]} #{deputies[0]}", str(deputies[0])))
except:
    print("No employees in model")

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
                                             default="None",
                                             blank=True)
    commandOne_second_four = models.CharField(max_length=30,
                                              choices=EMPLOYEE_CHOICES,
                                              default="None",
                                              blank=True)
    commandOne_third_four = models.CharField(max_length=30,
                                             choices=EMPLOYEE_CHOICES,
                                             default="None",
                                             blank=True)

    commandTwo_first_four = models.CharField(max_length=30,
                                             choices=EMPLOYEE_CHOICES,
                                             default="None",
                                             blank=True)
    commandTwo_second_four = models.CharField(max_length=30,
                                              choices=EMPLOYEE_CHOICES,
                                              default="None",
                                              blank=True)
    commandTwo_third_four = models.CharField(max_length=30,
                                             choices=EMPLOYEE_CHOICES,
                                             default="None",
                                             blank=True)

    north_first_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        default="None",
                                        blank=True)
    north_second_four = models.CharField(max_length=30,
                                         choices=EMPLOYEE_CHOICES,
                                         default="None",
                                         blank=True)
    north_third_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        default="None",
                                        blank=True)

    west_first_four = models.CharField(max_length=30,
                                       choices=EMPLOYEE_CHOICES,
                                       default="None",
                                       blank=True)
    west_second_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        default="None",
                                        blank=True)
    west_third_four = models.CharField(max_length=30,
                                       choices=EMPLOYEE_CHOICES,
                                       default="None",
                                       blank=True)

    cover_first_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        default="None",
                                        blank=True)
    cover_second_four = models.CharField(max_length=30,
                                         choices=EMPLOYEE_CHOICES,
                                         default="None",
                                         blank=True)
    cover_third_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        default="None",
                                        blank=True)

    east_first_four = models.CharField(max_length=30,
                                       choices=EMPLOYEE_CHOICES,
                                       default="None",
                                       blank=True)
    east_second_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        default="None",
                                        blank=True)
    east_third_four = models.CharField(max_length=30,
                                       choices=EMPLOYEE_CHOICES,
                                       default="None",
                                       blank=True)

    south_first_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        default="None",
                                        blank=True)
    south_second_four = models.CharField(max_length=30,
                                         choices=EMPLOYEE_CHOICES,
                                         default="None",
                                         blank=True)
    south_third_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        default="None",
                                        blank=True)
