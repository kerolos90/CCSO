from django.contrib import admin
from .models import Employees
# Register your models here.



class EmployeesAdmin(admin.ModelAdmin):
    exclude = ("password",)
    list_filter = ("title", "fto",)
    list_display = ("id", "title", "f_name", "l_name",
                    "email", "fto", "admin", )


admin.site.register(Employees, EmployeesAdmin)
