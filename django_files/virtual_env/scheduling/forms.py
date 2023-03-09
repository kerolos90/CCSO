from django import forms
from .models import *

class TimeOffRequestForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateTimeInput(
        attrs={'type': 'datetime-local', 'class': 'form-control'}))
    end_date = forms.DateField(widget=forms.DateTimeInput(
        attrs={'type': 'datetime-local', 'class': 'form-control'}))


class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseModelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-select'})
            self.fields[field].initial = self.fields[field]

class EditScheduleForm(BaseModelForm):
    class Meta:
        model = GoldDays
        exclude = ['date']

class ShiftCommanderOneForm(BaseModelForm):
    class Meta:
        model = ShiftCommanderTwo
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

 