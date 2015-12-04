from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from csp.decorators import csp_exempt
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .models import *
from .forms import PatientForm, TreatmentForm

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
    return render(request, 'core/scoreboard.html')

@csp_exempt
@csrf_exempt
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def pill_taken(request):
    return Response(status=200, data='{\'deu\': \'certo\'}', content_type='application/json')