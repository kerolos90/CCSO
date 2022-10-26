from django import forms

class TimeOffRequestForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateTimeInput(attrs={'type':'datetime-local','class':'form-control'}))
    end_date = forms.DateField(widget=forms.DateTimeInput(attrs={'type':'datetime-local','class':'form-control'}))