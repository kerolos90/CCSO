from django import forms
from .models import *

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

class ShiftCommanderOneForm(forms.ModelForm):
    class Meta:
        model = ShiftCommanderOne
        exclude = ['date']
   
    def __init__(self, *args, **kwargs):
        super(ShiftCommanderOneForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-select'})
            self.fields[field].initial = self.fields[field]

class ShiftCommanderTwoForm(forms.ModelForm):
    class Meta:
        model = ShiftCommanderTwo
        exclude = ['date']
   
    def __init__(self, *args, **kwargs):
        super(ShiftCommanderTwoForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-select'})
            self.fields[field].initial = self.fields[field]

class ShiftCommanderOneForm(forms.ModelForm):
    class Meta:
        model = ShiftCommanderOne
        exclude = ['date']
   
    def __init__(self, *args, **kwargs):
        super(ShiftCommanderOneForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-select'})
            self.fields[field].initial = self.fields[field]

class ShiftCommanderOneForm(forms.ModelForm):
    class Meta:
        model = ShiftCommanderOne
        exclude = ['date']
   
    def __init__(self, *args, **kwargs):
        super(ShiftCommanderOneForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-select'})
            self.fields[field].initial = self.fields[field]

class ShiftCommanderOneForm(forms.ModelForm):
    class Meta:
        model = ShiftCommanderOne
        exclude = ['date']
   
    def __init__(self, *args, **kwargs):
        super(ShiftCommanderOneForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-select'})
            self.fields[field].initial = self.fields[field]

class ShiftCommanderOneForm(forms.ModelForm):
    class Meta:
        model = ShiftCommanderOne
        exclude = ['date']
   
    def __init__(self, *args, **kwargs):
        super(ShiftCommanderOneForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-select'})
            self.fields[field].initial = self.fields[field]

class ShiftCommanderOneForm(forms.ModelForm):
    class Meta:
        model = ShiftCommanderOne
        exclude = ['date']
   
    def __init__(self, *args, **kwargs):
        super(ShiftCommanderOneForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-select'})
            self.fields[field].initial = self.fields[field]

class ShiftCommanderOneForm(forms.ModelForm):
    class Meta:
        model = ShiftCommanderOne
        exclude = ['date']
   
    def __init__(self, *args, **kwargs):
        super(ShiftCommanderOneForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-select'})
            self.fields[field].initial = self.fields[field]

class ShiftCommanderOneForm(forms.ModelForm):
    class Meta:
        model = ShiftCommanderOne
        exclude = ['date']
   
    def __init__(self, *args, **kwargs):
        super(ShiftCommanderOneForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-select'})
            self.fields[field].initial = self.fields[field]

class ShiftCommanderOneForm(forms.ModelForm):
    class Meta:
        model = ShiftCommanderOne
        exclude = ['date']
   
    def __init__(self, *args, **kwargs):
        super(ShiftCommanderOneForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-select'})
            self.fields[field].initial = self.fields[field]

class ShiftCommanderOneForm(forms.ModelForm):
    class Meta:
        model = ShiftCommanderOne
        exclude = ['date']
   
    def __init__(self, *args, **kwargs):
        super(ShiftCommanderOneForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-select'})
            self.fields[field].initial = self.fields[field]

class ShiftCommanderOneForm(forms.ModelForm):
    class Meta:
        model = ShiftCommanderOne
        exclude = ['date']
   
    def __init__(self, *args, **kwargs):
        super(ShiftCommanderOneForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-select'})
            self.fields[field].initial = self.fields[field]

class ShiftCommanderOneForm(forms.ModelForm):
    class Meta:
        model = ShiftCommanderOne
        exclude = ['date']
   
    def __init__(self, *args, **kwargs):
        super(ShiftCommanderOneForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-select'})
            self.fields[field].initial = self.fields[field]
 