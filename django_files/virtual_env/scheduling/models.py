from django.db import models

# Create your models here.

class Employees(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.title} {self.f_name} {self.l_name}"