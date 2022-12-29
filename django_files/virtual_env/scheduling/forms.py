from django import forms
from .models import GoldDays

class TimeOffRequestForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateTimeInput(
        attrs={'type': 'datetime-local', 'class': 'form-control'}))
    end_date = forms.DateField(widget=forms.DateTimeInput(
        attrs={'type': 'datetime-local', 'class': 'form-control'}))


class EditScheduleForm(forms.ModelForm):
    class Meta:
        model = GoldDays
        exclude = ['date']
   
    def __init__(self, *args, **kwargs):
        super(EditScheduleForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-select'})
            self.fields[field].initial = self.fields[field]
