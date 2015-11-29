from rest_framework import viewsets

from .models import *
from .serializers import *

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset =  Doctor.objects.all()
    serializer_class = DoctorSerializer

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class RecurrentTreatmentViewSet(viewsets.ModelViewSet):
    queryset = RecurrentTreatment.objects.all()
    serializer_class = RecurrentTreatmentSerializer

class OneOffTreatmentViewSet(viewsets.ModelViewSet):
    queryset = OneOffTreatment.objects.all()
    serializer_class = OneOffTreatmentSerializer

class PillTakenViewSet(viewsets.ModelViewSet):
    queryset = PillTaken.objects.all()
    serializer_class = PillTakenSerializer