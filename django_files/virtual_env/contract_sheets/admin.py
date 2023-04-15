from django.contrib import admin
from .models import ContractSheet
# Register your models here.


class ContractSheetAdmin(admin.ModelAdmin):
    list_filter = ("date",)


admin.site.register(ContractSheet, ContractSheetAdmin)
