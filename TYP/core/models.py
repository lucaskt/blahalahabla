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
        today = date.today()
        return today.year - self.birth.year - ((today.month, today.day) < (self.birth.month, self.birth.day))

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
    tag = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class BaseTreatment(models.Model):
    patient = models.ForeignKey('Patient')
    doctor = models.ForeignKey('Doctor')
    medicine = models.ForeignKey('Medicine')
    start_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class RecurrentTreatment(BaseTreatment):
    time_interval = models.IntegerField(default=0)
    start_time = models.TimeField(null=True, blank=True)

    def __unicode__(self):
        return 'RecurrentTreatment {} - {}'.format(self.patient.first_name, self.medicine.name)

class OneOffTreatment(BaseTreatment):

    def __unicode__(self):
        return 'OneOffTreatment {} - {}'.format(self.patient.first_name, self.medicine.name)

class PillTaken(models.Model):
    patient = models.ForeignKey('Patient')
    medicine = models.ForeignKey('Medicine')
    taken_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'Pill taken by {} at {}'.format(self.treatment.patient.first_name, self.taken_at)