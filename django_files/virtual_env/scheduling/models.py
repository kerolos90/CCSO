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


date = models.DateField(
                        auto_now_add=False, auto_now=False, primary_key=True, blank=False)
def hour_blocks(): 
    return  models.CharField(max_length=30,choices=EMPLOYEE_CHOICES,blank=True)

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
    date = models.DateField(
        auto_now_add=False, auto_now=False, primary_key=True, blank=False)
    first_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    second_four = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, blank=True)
    
class GoldDays(models.Model):
    date = models.DateField(
        auto_now_add=False, auto_now=False, primary_key=True, blank=False)

    commandOne_first_four = models.CharField(max_length=30,
                                             choices=EMPLOYEE_CHOICES,
                                             blank=True)
    commandOne_second_four = models.CharField(max_length=30,
                                              choices=EMPLOYEE_CHOICES,
                                              blank=True)
    commandOne_third_four = models.CharField(max_length=30,
                                             choices=EMPLOYEE_CHOICES,
                                             blank=True)
    
    commandTwo_first_four = models.CharField(max_length=30,
                                             choices=EMPLOYEE_CHOICES,
                                             blank=True)
    commandTwo_second_four = models.CharField(max_length=30,
                                              choices=EMPLOYEE_CHOICES,
                                              blank=True)
    commandTwo_third_four = models.CharField(max_length=30,
                                             choices=EMPLOYEE_CHOICES,
                                             blank=True)

    north_first_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        blank=True)
    north_second_four = models.CharField(max_length=30,
                                         choices=EMPLOYEE_CHOICES,
                                         blank=True)
    north_third_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        blank=True)

    west_first_four = models.CharField(max_length=30,
                                       choices=EMPLOYEE_CHOICES,
                                       blank=True)
    west_second_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        blank=True)
    west_third_four = models.CharField(max_length=30,
                                       choices=EMPLOYEE_CHOICES,
                                       blank=True)

    cover_first_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        blank=True)
    cover_second_four = models.CharField(max_length=30,
                                         choices=EMPLOYEE_CHOICES,
                                         blank=True)
    cover_third_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        blank=True)

    east_first_four = models.CharField(max_length=30,
                                       choices=EMPLOYEE_CHOICES,
                                       blank=True)
    east_second_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        blank=True)
    east_third_four = models.CharField(max_length=30,
                                       choices=EMPLOYEE_CHOICES,
                                       blank=True)

    south_first_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        blank=True)
    south_second_four = models.CharField(max_length=30,
                                         choices=EMPLOYEE_CHOICES,
                                         blank=True)
    south_third_four = models.CharField(max_length=30,
                                        choices=EMPLOYEE_CHOICES,
                                        blank=True)
