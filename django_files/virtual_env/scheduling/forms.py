from django import forms
from .models import *

class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseModelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-select'})
            self.fields[field].initial = self.fields[field]

class ShiftCommanderOneForm(BaseModelForm):
    class Meta:
        model = ShiftCommanderOne
        exclude = ['date']
             
class ShiftCommanderTwoForm(BaseModelForm):
    class Meta:
        model = ShiftCommanderTwo
        exclude = ['date']
   
class NorthForm(BaseModelForm):
    class Meta:
        model = North
        exclude = ['date']

class WestForm(BaseModelForm):
    class Meta:
        model = West
        exclude = ['date']

class EastForm(BaseModelForm):
    class Meta:
        model = East
        exclude = ['date']

class CoverForm(BaseModelForm):
    class Meta:
        model = Cover
        exclude = ['date']

class SouthForm(BaseModelForm):
    class Meta:
        model = South
        exclude = ['date']

class SaintJosephForm(BaseModelForm):
    class Meta:
        model = SaintJoseph
        exclude = ['date']

class SavoyOneForm(BaseModelForm):
    class Meta:
        model = SavoyOne
        exclude = ['date']

class SavoyTwoForm(BaseModelForm):
    class Meta:
        model = SavoyTwo
        exclude = ['date']

class SavoyThreeForm(BaseModelForm):
    class Meta:
        model = SavoyThree
        exclude = ['date']

class CivilServiceOneForm(BaseModelForm):
    class Meta:
        model = CivilServiceOne
        exclude = ['date']

class CivilServiceTwoForm(BaseModelForm):
    class Meta:
        model = CivilServiceOne
        exclude = ['date']

class OtherForm(forms.ModelForm):
    class Meta:
        model = Other
        exclude = ['date']
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    beat_assignment = forms.ChoiceField(choices=ACTIVITY_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    employee = forms.ChoiceField(choices=EMPLOYEE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    start_time = forms.TimeField(required=False, widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}))
    end_time = forms.TimeField(required=False, widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}))

class TimeOffRequestForm(forms.ModelForm):
    class Meta:
        model = TimeOffRequest
        exclude = ['submitted', 'status', 'reviewed', 'supervisor_comment']
    employee = forms.CharField(required=False, widget=forms.HiddenInput())
    start_time = forms.TimeField(widget=forms.TimeInput(
        attrs={'type': 'time', 'class': 'form-control', 'value': '00:00'}))
    end_time = forms.TimeField(widget=forms.TimeInput(
        attrs={'type': 'time', 'class': 'form-control', 'value': '00:00'}))
    vacation = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'number-only form-control', 'value': '0'}))
    comp = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'number-only form-control', 'value': '0'}))
    holiday= forms.CharField(widget=forms.TextInput(
        attrs={'class': 'number-only form-control', 'value': '0'}))
    sick = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'number-only form-control', 'value': '0'}))
    personal = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'number-only form-control', 'value': '0'}))
    comment = forms.CharField(widget = forms.TextInput(
        attrs={'class': 'form-control'}))

class SupervisorTimeOffReviewForm(forms.ModelForm):
    class Meta:
        model = TimeOffRequest
        fields = ['id','status', 'supervisor','supervisor_comment']
    supervisor = forms.CharField(widget=forms.HiddenInput())
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    status = forms.ChoiceField(choices=[('Approved', 'Approved'), ('Denied', 'Denied'),],
                               widget=forms.Select(attrs={'class': 'form-select'}))
    supervisor_comment = forms.CharField(widget = forms.TextInput(
        attrs={'class': 'form-control'}))
        