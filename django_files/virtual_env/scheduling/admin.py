from django.contrib import admin
from .models import EmpAssignment
# Register your models here.


class TeamsAdmin(admin.ModelAdmin):
    list_filter = ("assignment", )
    list_display = ("assignment", )



admin.site.register(EmpAssignment, TeamsAdmin)
