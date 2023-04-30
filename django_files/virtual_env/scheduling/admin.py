from django.contrib import admin
from .models import *
# Register your models here.



class ShiftCommanderOneAdmin(admin.ModelAdmin):
    list_filter = ("date",)

admin.site.register(ShiftCommanderOne, ShiftCommanderOneAdmin)


class TimeOffRequestAdmin(admin.ModelAdmin):
    list_display = ("date", 'id')

admin.site.register(TimeOffRequest, TimeOffRequestAdmin)
