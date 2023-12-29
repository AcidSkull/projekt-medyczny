from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelChoiceField
from django.utils.timezone import now

# Create your models here.

def user_str(self):
    return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'
User.add_to_class('__str__', user_str)

class Patient(models.Model):

    first_name = models.CharField(max_length=50, blank=True, default=None)
    last_name = models.CharField(max_length=50, blank=True, default=None)
    pesel = models.CharField(max_length=11, null=True, blank=True, default='')
    date_of_birth = models.DateField(null=True, blank=True, default=now())
    sex = models.CharField(null=True, blank=True, default=True)
    telephone = models.CharField(max_length=15, null=True, blank=True, default='')
    blood_group = models.CharField(max_length=3, null=True, blank=True, default='')
    chronic_diseases = models.CharField(max_length=50, null=True, blank=True, default='')
    medical_allergy = models.CharField(max_length=50, null=True, blank=True, default='')
    address_city = models.CharField(max_length=30, null=True, blank=True, default='')
    address_number = models.CharField(max_length=5, null=True, blank=True, default='')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Appointment(models.Model):

    doctor_id = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(default=now())
    goal_of_appointment = models.CharField()

    def __str__(self):
        return ''

class Diagnosis(models.Model):
    doctor_id = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    admission_date = models.DateField(default=now())
    reasons_for_admission = models.CharField(max_length=255, null=True, blank=True, default='')
    diagnostic_tests = models.CharField(max_length=255, null=True, blank=True, default='')
    diagnosis = models.CharField(max_length=50, null=True, blank=True, default='')
    treatment_plan = models.CharField(max_length=512, null=True, blank=True, default='')
    def __str__(self):
        return ''

class Ward(models.Model):
    name = models.CharField(max_length=50)

class Unit(models.Model):
    name = models.CharField(max_length=25, null=True, blank=True, default='')
    ward_id = models.ForeignKey(Ward, on_delete=models.CASCADE)

class HospitalStay(models.Model):
    admission_date = models.DateField(null=True, blank=True, default=now())
    discharge_date = models.DateField(null=True, blank=True, default=None)
    medical_procedures = models.CharField(max_length=512, null=True, blank=True, default='')
    doctor_id = models.ForeignKey(User, on_delete=models.CASCADE)
    additional_info = models.CharField(max_length=512, null=True, blank=True, default='')
    diagnosis_id = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Unit, on_delete=models.CASCADE)
    ward_id = models.ForeignKey(Ward, on_delete=models.CASCADE)

    def __str__(self):
        return ''