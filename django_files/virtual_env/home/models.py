from email.policy import default
from random import choices
from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser

# Create your models here.
TITLE_CHOICES = [
    ("admin", "admin"),
    ("Deputy", "Deputy"),
    ("Investigator", "Investigator"),
    ("Sergeant", "Sergeant"),
    ("Lieutenant", "Lieutenant"),
    ("Captain", "Captain"),
    ("Deputy Chief", "Deputy Chief"),
    ("Sheriff", "Sheriff"),
]

ASSIGNMENT_CHOICES = [
    ("None", "None"),
    ("Gold Days", "Gold Days"),
    ("Gold Nights", "Gold Nights"),
    ("Brown Days", "Brown Days"),
    ("Brown Nights", "Brown Nights"),
    ("St. Joseph", "St. Joseph"),
    ("Savoy", "Savoy"),
    ("Civil Process", "Civil Process"),
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

class User(AbstractUser):
    badge_number = models.IntegerField(default=500)
    title = models.CharField(
        max_length=20,
        choices=TITLE_CHOICES
    )
    start_date = models.DateField(default= "2023-04-25")
    phone_number = PhoneField(blank=True, help_text='Contact phone number')

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

    field_training_officer = models.BooleanField(default=False)
    canine = models.BooleanField(default=False)
    crime_scene_investigator = models.BooleanField(default=False)
    hostage_negotiator = models.BooleanField(default=False)
    firearms_instructor = models.BooleanField(default=False)


EMPLOYEE_CHOICES = []

try:
    for employee in User.objects.order_by('badge_number').values_list('badge_number', 'title', 'last_name'):
        if (employee[1] != 'admin'):
            EMPLOYEE_CHOICES.append(
                (f"{employee[1]} {employee[2]} #{employee[0]}", f"#{employee[0]}"))
except:
    print("No employees in database")

