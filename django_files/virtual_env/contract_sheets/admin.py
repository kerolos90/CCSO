from django.contrib import admin
from .models import Ivesdale
# Register your models here.

class IvesdaleAdmin(admin.ModelAdmin):
    list_filter = ("date",)

admin.site.register(Ivesdale, IvesdaleAdmin)
