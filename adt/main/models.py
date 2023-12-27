from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelChoiceField

# Create your models here.
class PatientPost(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pesel = models.CharField(max_length=11)
    date_of_birth = models.DateField()
    sex = models.CharField()
    telephone = models.CharField(max_length=15)
    blood_group = models.CharField(max_length=3)
    chronic_diseases = models.CharField(max_length=50)
    medical_allergy = models.CharField(max_length=50)
    address_city = models.CharField(max_length=30)
    address_number = models.CharField(max_length=5)

    def __str__(self):
        return self.first_name + ' ' + self.last_name