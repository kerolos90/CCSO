from django.contrib import admin
from .models import EmpAssignment
# Register your models here.


class TeamsAdmin(admin.ModelAdmin):
    list_filter = ("assignment", )
    list_display = ("get_employee","assignment", "short_day")
    @admin.display(ordering='employee__id', description='Employee')
    def get_employee(self,obj):
        return f"{obj.employee.title} {obj.employee.l_name} #{obj.employee.id}"


admin.site.register(EmpAssignment, TeamsAdmin)
