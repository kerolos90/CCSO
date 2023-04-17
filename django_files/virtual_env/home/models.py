from email.policy import default
from random import choices
from django.db import models
from phone_field import PhoneField

#from scheduling.models import EmpAssignment

# Create your models here.


class Employees(models.Model):
    TITLE_CHOICES = [
        ("Deputy", "Deputy"),
        ("Investigator", "Investigator"),
        ("Sergeant", "Sergeant"),
        ("Lieutenant", "Lieutenant"),
        ("Captain", "Captain"),
        ("Deputy Chief", "Deputy Chief"),
        ("Sheriff", "Sheriff"),
    ]

    id = models.IntegerField(
        primary_key=True,
        default=501
        )
    title = models.CharField(
        max_length=20,
        choices=TITLE_CHOICES
        )
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    fto = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')

    #start date

    def __str__(self) -> str:
        return f"{self.id} {self.title} {self.f_name} {self.l_name} {self.email} {self.password} {self.fto} {self.admin}"

    class Meta:
        verbose_name_plural = "Employees"
