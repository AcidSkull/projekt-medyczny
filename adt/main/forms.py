from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User, Group
from django.forms import SelectDateWidget, DateField, ChoiceField, ModelChoiceField
from .models import *


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class PatientForm(forms.ModelForm):
    date_of_birth = DateField(widget=SelectDateWidget)
    sex = ChoiceField(choices=[(True, 'Male'), (False, 'Female')])
    status = ChoiceField(choices=[('Discharge', 'Discharge'), ('Admission', 'Admission'), ('Permit', 'Permit')])

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'id_number', 'date_of_birth', 'sex', 'telephone',
                  'blood_group', 'chronic_diseases', 'medical_allergy', 'address_city', 'address_number',
                  'status']


class AppointmentForm(forms.ModelForm):
    doctor = ModelChoiceField(queryset=User.objects.filter(groups__name='Doctors'))
    patient = ModelChoiceField(queryset=Patient.objects.all())

    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'date', 'goal_of_appointment']


class DiagnosisForm(forms.ModelForm):
    doctor_id = ModelChoiceField(queryset=User.objects.all())
    patient_id = ModelChoiceField(queryset=Patient.objects.all())
    diagnostic_code = ModelChoiceField(queryset=DiagnosisCode.objects.all())

    class Meta:
        model = Diagnosis
        fields = ['doctor_id', 'patient_id', 'admission_date', 'reasons_for_admission',
                  'diagnostic_tests', 'diagnosis', 'treatment_plan', 'diagnosis_code']


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
    hospital_id = ModelChoiceField(queryset=Hospital.objects.all())

    class Meta:
        model = Branch
        fields = ['name', 'hospital_id']


class RoomForm(forms.ModelForm):
    branch_id = ModelChoiceField(queryset=Branch.objects.all())

    class Meta:
        model = Room
        fields = ['name', 'number_of_beds', 'branch_id']


class HospitalStayForm(forms.ModelForm):
    doctor_id = ModelChoiceField(queryset=User.objects.all())
    patient_id = ModelChoiceField(queryset=Patient.objects.all())
    diagnosis_id = ModelChoiceField(queryset=Diagnosis.objects.all())
    room_id = ModelChoiceField(queryset=Room.objects.all())

    class Meta:
        model = HospitalStay
        fields = ['admission_date', 'discharge_date', 'medical_procedures',
                  'doctor_id', 'additional_info', 'diagnosis_id', 'patient_id',
                  'room_id']
