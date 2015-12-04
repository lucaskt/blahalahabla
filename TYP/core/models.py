from datetime import date
from django.db import models

class Patient(models.Model):
    device_key = models.CharField(max_length=255, null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=128, null=True)
    last_name = models.CharField(max_length=128, null=True)
    birth = models.DateField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def age(self):
        if self.birth is not None:
            today = date.today()
            return today.year - self.birth.year - ((today.month, today.day) < (self.birth.month, self.birth.day))
        return 0

    def __unicode__(self):
        return '[{}] {} - {}'.format(self.device_key, self.first_name, self.age)


class Doctor(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Medicine(models.Model):
    name = models.CharField(max_length=128)
    tag = models.CharField(max_length=128, unique=True)
    dosage = models.CharField(max_length=128, default="")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class RecurringTreatment(models.Model):
    patient = models.ForeignKey('Patient', related_name='treatments')
    doctor = models.ForeignKey('Doctor', related_name='treatments')
    medicine = models.ForeignKey('Medicine', related_name='treatments')
    shots = models.IntegerField(default=0)

    time_interval = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return 'RecurrentTreatment {} - {}'.format(self.patient.first_name, self.medicine.name)

class PillTaken(models.Model):
    patient = models.ForeignKey('Patient', related_name='pills_taken')
    medicine = models.ForeignKey('Medicine', related_name='pills_taken')
    taken_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'Pill taken by {} at {}'.format(self.patient.first_name, self.taken_at)