from django import forms

from .models import *

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['device_key', 'first_name', 'last_name', 'birth']

class TreatmentForm(forms.ModelForm):
    class Meta:
        model = RecurringTreatment
        fields = ['doctor', 'medicine', 'patient', 'time_interval']