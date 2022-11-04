from django import forms
from home.models import Employees
class TimeOffRequestForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateTimeInput(attrs={'type':'datetime-local','class':'form-control'}))
    end_date = forms.DateField(widget=forms.DateTimeInput(attrs={'type':'datetime-local','class':'form-control'}))

class EditScheduleForm(forms.Form):
    class Meta:
        model = Employees