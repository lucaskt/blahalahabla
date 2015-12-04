from math import ceil
from json import loads

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions

from .models import *
from .forms import PatientForm, TreatmentForm

from score import Score

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

def scoreboard(request):
    score = generate_scores()
    return render(request, 'core/scoreboard.html', {'scores': score})

def generate_scores():
    scoreList = []
    for p in Patient.objects.all():
        total = 0
        count = 0
        for m in Medicine.objects.filter(treatments__patient=p).distinct():
            r = RecurringTreatment.objects.get(patient = p, medicine = m)
            pt = PillTaken.objects.filter(patient = p, medicine = m)
            s = Score()
            total = total + s.translate(r, pt)
            count = count + 1
        total = ceil(total / count)if count > 0 else 0
        scoreList.append({p: total})
    return scoreList

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def pill_taken(request):

    pill = PillTaken()
    pill.medicine = Medicine.objects.get(tag=request.POST['medicinekey'])
    pill.patient = Patient.objects.get(device_key=request.POST['devicekey'])
    pill.save()

    return Response(status=200)
