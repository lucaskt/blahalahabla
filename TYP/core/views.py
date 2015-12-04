from django.shortcuts import render

from .models import Patient

def index(request):
    return render(request, 'core/base.html')

def patients(request):
    patients_all = Patient.objects.all()
    return render(request, 'core/patients.html', {'patients': patients_all})

def scoreboard(request):
    return render(request, 'core/scoreboard.html')