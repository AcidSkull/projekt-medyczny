from django.shortcuts import render, redirect
from .forms import RegisterForm, PatientForm, AppointmentForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from .models import *

# Create your views here.
@login_required(login_url='/login')
def home(request):
    return render(request, 'main/home.html')

@login_required(login_url='/login')
def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = PatientForm()

    return render(request, 'main/create.html', {"form": form})

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {'form': form})

@login_required(login_url='/login')
def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = AppointmentForm()

    return render(request, 'main/create.html', {"form": form})

@login_required(login_url='/login')
def patient(request, id):
    if request.method == 'POST':
        post_id = request.POST.get("post-id")
        patient_to_delete = Patient.objects.filter(id=post_id).first()
        if patient_to_delete:
            patient_to_delete.delete()
        return redirect('home')
    else:
        patient = Patient.objects.filter(id=id).values()
        if len(patient) == 1:
            return render(request, 'main/patient.html', {"patient": patient[0]})
        else:
            return HttpResponseNotFound("Patient not found!")