from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User, Group
from django.forms import SelectDateWidget, DateField, ChoiceField, ModelChoiceField, Textarea, DateInput
from .models import *

class DateInputButBetter(DateInput):
    input_type = 'date'

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    group = ChoiceField(choices=[('Doctor', 'Doctor'), ('Receptionist', 'Receptionist')])
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'group']


class PatientForm(forms.ModelForm):
    sex = ChoiceField(choices=[(True, 'Male'), (False, 'Female')])
    status = ChoiceField(choices=[('Discharge', 'Discharge'), ('Admission', 'Admission'), ('Permit', 'Permit')])

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'id_number', 'date_of_birth', 'sex', 'telephone',
                  'blood_group', 'chronic_diseases', 'medical_allergy', 'address_city', 'address_number',
                  'status']
        widgets = {
            'date_of_birth' : DateInputButBetter,
            'chronic_diseases' : Textarea,
            'medical_allergy' : Textarea,
        }


class AppointmentForm(forms.ModelForm):
    doctor = ModelChoiceField(queryset=User.objects.filter(groups__name='Doctors'))
    patient = ModelChoiceField(queryset=Patient.objects.all())

    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'date', 'goal_of_appointment']
        widgets = {
            'goal_of_appointment' : Textarea,
            'date' : DateInputButBetter,
        }


class DiagnosisForm(forms.ModelForm):
    doctor = ModelChoiceField(queryset=User.objects.filter(groups__name='Doctors'))
    patient = ModelChoiceField(queryset=Patient.objects.all())
    diagnosis_code = ModelChoiceField(queryset=DiagnosisCode.objects.all())

    class Meta:
        model = Diagnosis
        fields = ['doctor', 'patient', 'admission_date', 'reasons_for_admission',
                  'diagnostic_tests', 'diagnosis', 'treatment_plan', 'diagnosis_code']
        widgets = {
            'admission_date' : DateInputButBetter,
        }


class DiagnosisCodeForm(forms.ModelForm):

    class Meta:
        model = DiagnosisCode
        fields = ['name', 'code']


class ProcedureCodForme(forms.ModelForm):
    class Meta:
        model = ProcedureCode
        fields = ['name', 'code']


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['name']


class BranchForm(forms.ModelForm):
    hospital = ModelChoiceField(queryset=Hospital.objects.all())

    class Meta:
        model = Branch
        fields = ['name', 'hospital']


class RoomForm(forms.ModelForm):
    branch = ModelChoiceField(queryset=Branch.objects.all())

    class Meta:
        model = Room
        fields = ['name', 'number_of_beds', 'branch']


class HospitalStayForm(forms.ModelForm):
    admission_date = DateField(widget=SelectDateWidget)
    discharge_date = DateField(widget=SelectDateWidget)
    doctor = ModelChoiceField(queryset=User.objects.filter(groups__name='Doctors'))
    patient = ModelChoiceField(queryset=Patient.objects.all())
    room = ModelChoiceField(queryset=Room.objects.all())

    class Meta:
        model = HospitalStay
        fields = ['admission_date', 'discharge_date', 'medical_procedures',
                  'doctor', 'additional_info', 'patient',
                  'room']
        widgets = {
            'admission_date' : DateInputButBetter,
            'discharge_date' : DateInputButBetter,
            'additional_info' : Textarea,
        }
