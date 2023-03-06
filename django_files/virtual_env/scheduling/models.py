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
    date = date
    first_four = hour_blocks()
    second_four = hour_blocks()
    third_four = hour_blocks()
    fourth_four = hour_blocks()
    fifth_four = hour_blocks()
    sixth_four = hour_blocks()

class ShiftCommanderTwo(models.Model):
    date = date
    first_four = hour_blocks()
    second_four = hour_blocks()
    third_four = hour_blocks()
    fourth_four = hour_blocks()
    fifth_four = hour_blocks()
    sixth_four = hour_blocks()

class North(models.Model):
    date = date
    first_four = hour_blocks()
    second_four = hour_blocks()
    third_four = hour_blocks()
    fourth_four = hour_blocks()
    fifth_four = hour_blocks()
    sixth_four = hour_blocks()

class West(models.Model):
    date = date
    first_four = hour_blocks()
    second_four = hour_blocks()
    third_four = hour_blocks()
    fourth_four = hour_blocks()
    fifth_four = hour_blocks()
    sixth_four = hour_blocks()

class East(models.Model):
    date = date
    first_four = hour_blocks()
    second_four = hour_blocks()
    third_four = hour_blocks()
    fourth_four = hour_blocks()
    fifth_four = hour_blocks()
    sixth_four = hour_blocks()

class Cover(models.Model):
    date = date
    first_four = hour_blocks()
    second_four = hour_blocks()
    third_four = hour_blocks()
    fourth_four = hour_blocks()
    fifth_four = hour_blocks()
    sixth_four = hour_blocks()

class South(models.Model):
    date = date
    first_four = hour_blocks()
    second_four = hour_blocks()
    third_four = hour_blocks()
    fourth_four = hour_blocks()
    fifth_four = hour_blocks()
    sixth_four = hour_blocks()

class SaintJoseph(models.Model):
    date = date
    first_four = hour_blocks()
    second_four = hour_blocks()

class SavoyOne(models.Model):
    date = date
    first_four = hour_blocks()
    second_four = hour_blocks()

class SavoyTwo(models.Model):
    date = date
    first_four = hour_blocks()
    second_four = hour_blocks()

class SavoyThree(models.Model):
    date = date
    first_four = hour_blocks()
    second_four = hour_blocks()

class CivilServiceOne(models.Model):
    date = date
    first_four = hour_blocks()
    second_four = hour_blocks()

class CivilServiceTwo(models.Model):
    date = date
    first_four = hour_blocks()
    second_four = hour_blocks()

class Other(models.Model):
    date = date
    first_four = hour_blocks()
    second_four = hour_blocks()
    
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
