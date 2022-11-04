from asyncio.windows_events import NULL
from random import choices
from django.db import models
#from home.models import Employees
# Create your models here.


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

    commandOne_first_four = models.CharField(max_length=100)
    commandOne_second_four = models.CharField(max_length=100)
    commandOne_third_four = models.CharField(max_length=100)
    commandOne_fourth_four = models.CharField(max_length=100)

    commandTwo_first_four = models.CharField(max_length=100)
    commandTwo_second_four = models.CharField(max_length=100)
    commandTwo_third_four = models.CharField(max_length=100)
    commandTwo_fourth_four = models.CharField(max_length=100)

    north_first_four = models.CharField(max_length=100)
    north_second_four = models.CharField(max_length=100)
    north_third_four = models.CharField(max_length=100)
    north_fourth_four = models.CharField(max_length=100)

    west_first_four = models.CharField(max_length=100)
    west_second_four = models.CharField(max_length=100)
    west_third_four = models.CharField(max_length=100)
    west_fourth_four = models.CharField(max_length=100)

    east_first_four = models.CharField(max_length=100)
    east_second_four = models.CharField(max_length=100)
    east_third_four = models.CharField(max_length=100)
    east_fourth_four = models.CharField(max_length=100)

    south_first_four = models.CharField(max_length=100)
    south_second_four = models.CharField(max_length=100)
    south_third_four = models.CharField(max_length=100)
    south_fourth_four = models.CharField(max_length=100)

    cover_first_four = models.CharField(max_length=100)
    cover_second_four = models.CharField(max_length=100)
    cover_third_four = models.CharField(max_length=100)
    cover_fourth_four = models.CharField(max_length=100)
