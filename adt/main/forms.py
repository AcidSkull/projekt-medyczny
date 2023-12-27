from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from django.forms import SelectDateWidget, DateField, ChoiceField
from .models import PatientPost

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PatientForm(forms.ModelForm):
    date_of_birth = DateField(widget=SelectDateWidget)
    sex = ChoiceField(choices=[(True, 'Male'), (False, 'Female')])
    class Meta:
        model = PatientPost
        fields = ['first_name', 'last_name', 'pesel', 'date_of_birth', 'sex', 'telephone',
                  'blood_group', 'chronic_diseases', 'medical_allergy', 'address_city', 'address_number']
