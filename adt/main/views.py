from django.shortcuts import render, redirect
from .forms import RegisterForm, PatientForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import PatientPost

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

    return render(request, 'main/create_patient.html', {"form": form})

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