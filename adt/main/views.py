from django.shortcuts import render, redirect
from .forms import RegisterForm, PatientForm, AppointmentForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404
from .models import *

def  get_model(name):
    if name == 'patient':
        return Patient
    elif name == 'appointment':
        return Appointment
    return None

def get_form(name, *args, **kwargs):
    if name == 'patient':
        return PatientForm(*args, **kwargs)
    elif name == 'appointment':
        return AppointmentForm(*args, **kwargs)
    return None


# Create your views here.
@login_required(login_url='/login')
def home(request):
    return render(request, 'main/home.html')

@login_required(login_url='/login')
def create(request, model_name):
    if request.method == 'POST':
        form = get_form(model_name, request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = get_form(model_name)

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
def view(request, model_name, id):
    if request.method == 'POST':
        post_id = request.POST.get("post-id")
        obj = get_model(model_name)
        obj.objects.filter(id=post_id).first()
        if obj:
            obj.delete()
        return redirect('home')
    else:
        obj = get_model(model_name)
        name = obj.__name__
        obj = obj.objects.filter(id=id).values()
        context = {"obj": obj[0], "name": name}

        if name == "Appointment":
            context['patient'] = Patient.objects.filter(id=context['obj']['patient_id'])[0]
            context['doctor'] = User.objects.filter(id=context['obj']['doctor_id'])[0]

        return render(request, 'main/view.html', context)

@login_required(login_url='/login')
def list(request, model_name):
    obj = get_model(model_name)
    content = obj.objects.all()

    return render(request, 'main/list.html', {'content': content, 'name': model_name})

@login_required(login_url='/login')
def edit(request, model_name, id):
    obj = get_object_or_404(get_model(model_name), id=id)

    if request.method == 'POST':
        form = get_form(model_name, request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(f'/view/{model_name}/{id}')
    else:
        form = get_form(model_name, instance=obj)
        return render(request, 'main/edit.html', {"form": form, "obj": obj})