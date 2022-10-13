from email.policy import default
from django.db import models

# Create your models here.

class Employees(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    assignment = models.CharField(max_length=50, blank=True)
    fto = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    #Phone number
    def __str__(self) -> str:
        return f"{self.id} {self.title} {self.f_name} {self.l_name} {self.email} {self.password} {self.assignment} {self.fto} {self.admin}"

    class Meta:
        verbose_name_plural = "Employees"
