from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.


class MyUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'badge_number', 'title',
                    'first_name', 'last_name',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('badge_number', 'title','first_name',
         'last_name', 'email','start_date','phone_number')}),
        ('Assignments', {'fields': ('assignment','short_day','field_training_officer',
                                    'canine','hostage_negotiator','firearms_instructor')}),
        ('Permissions', {'fields': ('is_active',
         'is_staff', 'groups', 'user_permissions')})
       
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('badge_number', 'title', 'start_date', 'assignment')}),
    )
    list_filter = ("is_staff",)

admin.site.register(User, MyUserAdmin)

