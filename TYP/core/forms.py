from django import forms

from .models import *

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['device_tag', 'first_name', 'last_name']