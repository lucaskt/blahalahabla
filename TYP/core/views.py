from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import *
from .forms import PatientForm, TreatmentForm

import Score
from math import ceil

def index(request):
    return render(request, 'core/base.html')

def patients(request):
    patients_all = Patient.objects.all()
    return render(request, 'core/patients.html', {'patients': patients_all})

def add_patient(request):
    if request.method == 'GET':
        form = PatientForm()
    elif request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('patients'))
    return render(request, 'core/add_patient.html', {'form': form})

def patient(request, patient_pk):
    p = Patient.objects.get(pk=patient_pk)
    return render(request, 'core/patient.html', {'patient': p})

def add_treatment(request, patient_pk):
    p = Patient.objects.get(pk=patient_pk)
    d = Doctor.objects.all()
    m = Medicine.objects.all()
    if request.method == 'GET':
        form = TreatmentForm()
    elif request.method == 'POST':
        form = TreatmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('patient', kwargs={'patient_pk': p.pk}))
    return render(request, 'core/add_treatment.html', {'form': form, 'patient': p, 'doctors': d, 'medicines': m})

def scoreboard(request, patient_pk):
    p = Patient.objects.get(pk = patient_pk)
    return render(request, 'core/scoreboard.html')

def generate_scores():
    scoreList = []
    for p in Patient.objects.all():
        total = 0
        count = 0
        for m in Medicine.objects.get(patient = p):
            r = RecurringTreatment.get(patient = p, medicine = m)
            pt = PillTaken.objects.get(patient = p, medicine = m)
            s = Score
            total = total + s.translate(r.time_interval, pt)
            count = count + 1
        total = ceil(total / count)
        scoreList.append({p: total})
    return scoreList
