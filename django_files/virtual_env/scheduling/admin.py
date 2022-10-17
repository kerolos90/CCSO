from django.contrib import admin
from .models import Patrol_Teams
# Register your models here.


class TeamsAdmin(admin.ModelAdmin):
    list_filter = ("team", )
    list_display = ("team", )



admin.site.register(Patrol_Teams, TeamsAdmin)
