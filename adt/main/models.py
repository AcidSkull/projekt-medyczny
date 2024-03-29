from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


def user_str(self):
    return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'

User.add_to_class('__str__', user_str)


class Patient(models.Model):

    first_name = models.CharField(max_length=50, blank=True, default=None)
    last_name = models.CharField(max_length=50, blank=True, default=None)
    id_number = models.CharField(max_length=11, null=True, blank=True, default='')
    date_of_birth = models.DateField(null=True, blank=True, default=now())
    sex = models.CharField(default=True)
    telephone = models.CharField(max_length=15, null=True, blank=True, default='')
    blood_group = models.CharField(max_length=3, null=True, blank=True, default='')
    chronic_diseases = models.CharField(max_length=50, null=True, blank=True, default='')
    medical_allergy = models.CharField(max_length=50, null=True, blank=True, default='')
    address_city = models.CharField(max_length=30, null=True, blank=True, default='')
    address_number = models.CharField(max_length=5, null=True, blank=True, default='')
    status = models.CharField(max_length=20, default='Discharge')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Appointment(models.Model):

    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(default=now())
    goal_of_appointment = models.CharField()

    def __str__(self):
        return str(self.date)


class DiagnosisCode(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, default='')
    code = models.CharField(max_length=50, null=True, blank=True, default='')

    def __str__(self):
        return self.name + ' (' + self.code + ')'


class ProcedureCode(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, default='')
    code = models.CharField(max_length=50, null=True, blank=True, default='')


class Diagnosis(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    admission_date = models.DateField(default=now())
    reasons_for_admission = models.CharField(max_length=255, null=True, blank=True, default='')
    diagnostic_tests = models.CharField(max_length=255, null=True, blank=True, default='')
    diagnosis = models.CharField(max_length=50, null=True, blank=True, default='')
    treatment_plan = models.CharField(max_length=512, null=True, blank=True, default='')
    diagnosis_code = models.ForeignKey(DiagnosisCode, on_delete=models.NOT_PROVIDED, null=True)

    def __str__(self):
        return ''


class Hospital(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=50)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=10)
    number_of_beds = models.CharField(max_length=5)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        branch_obj = Branch.objects.filter(id=self.branch.id)[0]
        hospital_obj = Hospital.objects.filter(id=branch_obj.hospital.id)[0]
        return hospital_obj.name + '. ' + branch_obj.name + ', ' + self.name


class HospitalStay(models.Model):
    admission_date = models.DateField(null=True, blank=True, default=now())
    discharge_date = models.DateField(null=True, blank=True, default=None)
    medical_procedures = models.CharField(max_length=512, null=True, blank=True, default='')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    additional_info = models.CharField(max_length=512, null=True, blank=True, default='')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.admission_date) + ' - ' + str(self.discharge_date)
