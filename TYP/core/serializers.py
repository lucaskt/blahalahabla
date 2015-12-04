from rest_framework import serializers

from .models import *

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('device_key', 'first_name', 'last_name', 'birth', 'age', 'created_at', 'updated_at')

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ('first_name', 'last_name', 'created_at', 'updated_at')

class MedicineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medicine
        fields = ('name', 'tag', 'created_at', 'updated_at')

class RecurringTreatmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = RecurringTreatment
        fields = ('doctor', 'medicine', 'time_interval', 'shots', 'created_at', 'updated_at')

class PillTakenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PillTaken
        fields = ('patient', 'medicine', 'taken_at')