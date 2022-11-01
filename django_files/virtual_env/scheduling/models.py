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
    assignment = models.CharField(
        max_length=20,
        choices =ASSIGNMENT_CHOICES,
        default = "None"
    )
    employee = models.ForeignKey('home.Employees', on_delete=models.CASCADE)
    short_day = models.CharField(max_length=20, blank=True)

class GoldDays(models.Model):
    date = models.DateField(
        auto_now_add=False, auto_now=False, primary_key=True, blank=False)

    commandOne_first_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    commandOne_second_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    commandOne_third_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    commandOne_fourth_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")

    commandTwo_first_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    commandTwo_second_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    commandTwo_third_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    commandTwo_fourth_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")

    north_first_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    north_second_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    north_third_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    north_fourth_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")

    west_first_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    west_second_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    west_third_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    west_fourth_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    
    east_first_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    east_second_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    east_third_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    east_fourth_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    
    south_first_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    south_second_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    south_third_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    south_fourth_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    
    cover_first_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    cover_second_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    cover_third_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")
    cover_fourth_four = models.ForeignKey(
        'home.Employees', on_delete=models.SET_DEFAULT, default="None")