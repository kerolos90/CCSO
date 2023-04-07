from django import forms
from .models import *


class HourMinSelectorWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        minutes_choices = [(i, f"{i:02d}") for i in range(0, 60, 15)]
        widgets = [
            forms.NumberInput(
                attrs={'class': 'form-control', 'min': 0, 'max': 23}),
            forms.Select(attrs={'class': 'form-select'},choices=minutes_choices),
        ]
        super().__init__(widgets, attrs)

    def decompress(self,value):
        if value:
            return [value.hours, value.minute]
        return [None, None]
    
class TimeSpentField(forms.MultiValueField):
    widget= HourMinSelectorWidget
    def __init__(self, *args, **kwargs):
        fields = (
            forms.IntegerField(min_value=0, max_value=23),
            forms.ChoiceField()
        )
        super(TimeSpentField,self).__init__(fields, *args, **kwargs)

    def compress(self, values):
        if values:
            return values[0]*60 + values[1]
            # return f"{values[0]:02d}:{values[1]:02d}"
        return None

class BaseForm(forms.ModelForm):
    hours = forms.IntegerField(min_value=0, max_value=24, required=True, 
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))
    minutes = forms.ChoiceField(choices=[(0, '00'), (15, '15'), (30, '30'), (45, '45')], 
                                widget=forms.Select(attrs={'class': 'form-select'}), required=True)
    
    class Meta:
        model = BaseModel
        exclude = ['id', 'submissionDate']

    employee = forms.ChoiceField(choices=EMPLOYEE_CHOICES, widget=forms.Select(
        attrs={'class': 'form-select'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class ': 'form-control'}))
    carNumber = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'style': 'width:65%'}))
    start_miles = forms.IntegerField(min_value=0, widget=forms.NumberInput(
        attrs={'id': 'start_miles', 'class': 'form-control' }))
    end_miles = forms.IntegerField(min_value=0, widget=forms.NumberInput(
        attrs={'id': 'end_miles', 'class': 'form-control'}))
    total_miles = forms.IntegerField(
        disabled=True, required=False, widget=forms.NumberInput(attrs={'id': 'total_miles'}))
    start_time = forms.TimeField(widget=forms.TimeInput(
        attrs={'id': 'start_time', 'type': 'time', 'class': 'form-control'}))
    end_time = forms.TimeField(widget=forms.TimeInput(
        attrs={'id': 'end_time', 'type': 'time', 'class': 'form-control'}))
    total_miles = forms.IntegerField(
        disabled=True, required=False, widget=forms.NumberInput(attrs={'id': 'total_time'}))
    weather = forms.ChoiceField(choices=[(
        'Clear', 'Clear'), ('Rain', 'Rain'), ('Snow', 'Snow')],
        widget=forms.Select(attrs={'class': 'form-select'}))
    
    patrolCar_timeSpent = TimeSpentField()
    patrolCar_activityLog = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    arrestTraffic_count = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    arrestTraffic_activityLog = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))

class IvesdaleForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = Ivesdale
