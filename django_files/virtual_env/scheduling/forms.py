from email.policy import default
from random import choices
from django import forms
from home.models import Employees
class TimeOffRequestForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateTimeInput(attrs={'type':'datetime-local','class':'form-control'}))
    end_date = forms.DateField(widget=forms.DateTimeInput(attrs={'type':'datetime-local','class':'form-control'}))

EMPOLYEE_CHOICES = [("502","502")]

class EditScheduleForm(forms.Form):
    north = forms.ChoiceField(choices=EMPOLYEE_CHOICES, widget = forms.Select(attrs= {'class': 'form-select'}) )
