from email.policy import default
from random import choices
from django import forms
from home.models import Employees
from .models import GoldDays

class TimeOffRequestForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateTimeInput(
        attrs={'type': 'datetime-local', 'class': 'form-control'}))
    end_date = forms.DateField(widget=forms.DateTimeInput(
        attrs={'type': 'datetime-local', 'class': 'form-control'}))


EMPLOYEE_CHOICES = [
    ("502", "502"),
    ("503", "503"),

]


class EditScheduleForm(forms.ModelForm):
    class Meta:
        model = GoldDays
        exclude = ['date']
   
    def __init__(self, *args, **kwargs):
        super(EditScheduleForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-select'})
            self.fields[field].initial = self.fields[field]
