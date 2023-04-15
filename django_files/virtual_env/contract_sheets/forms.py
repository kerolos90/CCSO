from django import forms
from .models import *


class HourMinSelectorWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        minutes_choices = [(i, f"{i:02d}") for i in range(0, 60, 15)]
        widgets = [
            forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 23, 'value': 0}),
            forms.Select(attrs={'class': 'form-select',}, choices=minutes_choices),
        ]
        super().__init__(widgets, attrs)

    def decompress(self,value):
        if value:
            return [value.hour , value.minute]
        return [None, None]
    
class TimeSpentField(forms.MultiValueField):
    widget= HourMinSelectorWidget()
    def __init__(self, *args, **kwargs):
        minutes_choices = [(i, f"{i:02d}") for i in range(0, 60, 15)]

        fields = (
            forms.IntegerField(),
            forms.ChoiceField(choices=minutes_choices)
        )
        super().__init__(fields=fields, *args, **kwargs)

    def compress(self, values):
        if values:
           return values[0] * 60 + int(values[1])
        return None

class ContractSheetForm(forms.ModelForm):

    class Meta:
        model = ContractSheet
        exclude = ['id', 'submissionDate']
    village = forms.CharField(widget=forms.HiddenInput())
    date = forms.DateField(widget=forms.HiddenInput())
    employee = forms.ChoiceField(disabled=False, choices=EMPLOYEE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    carNumber = forms.IntegerField(min_value=0,widget=forms.NumberInput(
        attrs={'class': 'form-control', 'style': 'width:65%', 'value':0}))
    start_miles = forms.IntegerField(min_value=0, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'value':0 }))        
    end_miles = forms.IntegerField(min_value=0, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'value':0}))
    total_miles = forms.IntegerField(widget=forms.HiddenInput(attrs={'value': 0}))
    start_time = forms.TimeField(widget=forms.TimeInput(
        attrs={'type': 'time', 'class': 'form-control', 'value': '00:00'}))
    end_time = forms.TimeField(widget=forms.TimeInput(
        attrs={'type': 'time', 'class': 'form-control', 'value': '00:00'}))
    total_time = forms.IntegerField(widget=forms.HiddenInput(attrs={'value': 0}))
    weather = forms.ChoiceField(choices=[(
        'Clear', 'Clear'), ('Rain', 'Rain'), ('Snow', 'Snow')],
        widget=forms.Select(attrs={'class': 'form-select'}))
    
    patrolCar_timeSpent = TimeSpentField()
    patrolCar_activityLog = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':2}))
    patrolFoot_timeSpent = TimeSpentField()
    patrolFoot_activityLog = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':2}))
    reportWriting_timeSpent = TimeSpentField()
    reportWriting_activityLog = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':2}))
    court_timeSpent = TimeSpentField()
    court_activityLog = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':2}))
    trafficDetail_timeSpent = TimeSpentField()
    trafficDetail_activityLog = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':2}))
    specialDetail_timeSpent = TimeSpentField()
    specialDetail_activityLog = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':2}))
    investigateAccident_timeSpent = TimeSpentField()
    investigateAccident_activityLog = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':2}))
    investigateCriminal_timeSpent = TimeSpentField()
    investigateCriminal_activityLog = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':2}))
    investigateOther_timeSpent = TimeSpentField()
    investigateOther_activityLog = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':2}))

    arrestTraffic_count = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'value': 0}))
    arrestTraffic_activityLog = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':2}))
    arrestCriminal_count = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'value': 0}))
    arrestCriminal_activityLog = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':2}))
    writtenWarnings_count = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'value': 0}))
    writtenWarnings_activityLog = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':2}))
    complaintsAnswered_count = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'value': 0}))
    complaintsAnswered_activityLog = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':2}))
    accidentsInvestigated_count = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'value': 0}))
    accidentsInvestigated_activityLog = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':2}))
    vehiclesInvolved_count = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'value': 0}))
    vehiclesInvolved_activityLog = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':2}))
    injuries_count = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'value': 0}))
    injuries_activityLog = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':2}))
    fatalities_count = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'value': 0}))
    fatalities_activityLog = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':2}))
    papersServed_count = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'value': 0}))
    papersServed_activityLog = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':2}))
    