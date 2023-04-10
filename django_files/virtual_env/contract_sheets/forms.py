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
   
    class Meta:
        model = BaseModel
        exclude = ['id', 'submissionDate']
    village = forms.CharField(widget=forms.HiddenInput())
    date = forms.DateField(disabled=False,widget=forms.DateInput(attrs={'type': 'date', 'class ': 'form-control'}))
    employee = forms.ChoiceField(disabled=True, choices=EMPLOYEE_CHOICES, widget=forms.Select(
        attrs={'class': 'form-select'}))
    carNumber = forms.IntegerField(min_value=1,widget=forms.NumberInput(
        attrs={'class': 'form-control', 'style': 'width:65%', 'value':0}))
    start_miles = forms.IntegerField(min_value=0, widget=forms.NumberInput(
        attrs={'id': 'start_miles', 'class': 'form-control', 'value':0 }))        
    end_miles = forms.IntegerField(min_value=0, widget=forms.NumberInput(
        attrs={'id': 'end_miles', 'class': 'form-control', 'value':0}))
    total_miles = forms.IntegerField(required=False, widget=forms.HiddenInput())
    start_time = forms.TimeField(widget=forms.TimeInput(
        attrs={'id': 'start_time', 'type': 'time', 'class': 'form-control'}))
    end_time = forms.TimeField(widget=forms.TimeInput(
        attrs={'id': 'end_time', 'type': 'time', 'class': 'form-control'}))
    total_time = forms.IntegerField(required=False, widget=forms.HiddenInput())
    weather = forms.ChoiceField(choices=[(
        'Clear', 'Clear'), ('Rain', 'Rain'), ('Snow', 'Snow')],
        widget=forms.Select(attrs={'class': 'form-select'}))
    
    patrolCar_timeSpent = TimeSpentField()
    patrolCar_activityLog = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    patrolFoot_timeSpent = TimeSpentField()
    patrolFoot_activityLog = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    reportWriting_timeSpent = TimeSpentField()
    reportWriting_activityLog = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    court_timeSpent = TimeSpentField()
    court_activityLog = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    trafficDetail_timeSpent = TimeSpentField()
    trafficDetail_activityLog = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    specialDetail_timeSpent = TimeSpentField()
    specialDetail_activityLog = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    investigateAccident_timeSpent = TimeSpentField()
    investigateAccident_activityLog = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    investigateCriminal_timeSpent = TimeSpentField()
    investigateCriminal_activityLog = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    investigateOther_timeSpent = TimeSpentField()
    investigateOther_activityLog = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))

    arrestTraffic_count = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    arrestTraffic_activityLog = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    arrestCriminal_count = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    arrestCriminal_activityLog = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    writtenWarnings_count = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    writtenWarnings_activityLog = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    complaintsAnswered_count = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    complaintsAnswered_activityLog = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    accidentsInvestigated_count = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    accidentsInvestigated_activityLog = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    vehiclesInvolved_count = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    vehiclesInvolved_activityLog = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    injuries_count = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    injuries_activityLog = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    fatalities_count = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    fatalities_activityLog = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    papersServed_count = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    papersServed_activityLog = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    
class IvesdaleForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = Ivesdale
