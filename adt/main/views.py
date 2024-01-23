from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import *

def  get_model(name):
    if name == 'patient':
        return Patient
    elif name == 'appointment':
        return Appointment
    elif name == 'diagnosis':
        return  Diagnosis
    elif name == 'hospital':
        return Hospital
    elif name == 'branch':
        return Branch
    elif name == 'room':
        return Room
    elif name == 'hospitalstay':
        return HospitalStay
    elif name == 'diagnosiscode':
        return DiagnosisCode

    return None

def get_form(name, *args, **kwargs):
    if name == 'patient':
        return PatientForm(*args, **kwargs)
    elif name == 'appointment':
        return AppointmentForm(*args, **kwargs)
    elif name == 'diagnosis':
        return  DiagnosisForm(*args, **kwargs)
    elif name == 'hospital':
        return HospitalForm(*args, **kwargs)
    elif name == 'branch':
        return BranchForm(*args, **kwargs)
    elif name == 'room':
        return RoomForm(*args, **kwargs)
    elif name == 'hospitalstay':
        return HospitalStayForm(*args, **kwargs)
    elif name == 'diagnosiscode':
        return DiagnosisCodeForm(*args, **kwargs)
    
    return None


# Create your views here.
@login_required(login_url='/login')
def home(request):
    return render(request, 'main/home.html')

@login_required(login_url='/login')
def create(request, model_name):
    if not request.user.has_perm(f'main.add_{model_name.lower()}'):
        return redirect('home')

    if request.method == 'POST':

        form = get_form(model_name, request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = get_form(model_name)

    return render(request, 'main/create.html', {"form": form, 'name': model_name})

@login_required(login_url='/login')
def sign_up(request):
    if not request.user.is_superuser:
        return redirect('home')

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name=request.POST.get('group'))
            if group is not None:
                user.groups.add(group)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {'form': form})

@login_required(login_url='/login')
def view(request, model_name, id):
    if not request.user.has_perm(f'main.view_{model_name.lower()}'):
       return redirect('home')

    if request.method == 'POST':
        if not request.user.has_perm(f'main.delete_{model_name.lower()}'):
            return redirect('home')

        post_id = request.POST.get("post-id")
        obj = get_model(model_name)
        obj.objects.filter(id=post_id).first()
        if obj:
            obj.objects.filter(id=id).delete()
        return redirect('home')
    else:
        obj = get_model(model_name)
        name = obj.__name__
        obj = obj.objects.filter(id=id).values()
        context = {"obj": obj[0], "name": name}

        if name == "Appointment" :
            context['patient'] = Patient.objects.filter(id=context['obj']['patient_id'])[0]
            context['doctor'] = User.objects.filter(id=context['obj']['doctor_id'])[0]
        elif name == 'Patient':
            context['diagnosis'] = Diagnosis.objects.filter(patient_id=context['obj']['id'])
            context['hospitalstay'] = HospitalStay.objects.filter(patient_id=context['obj']['id'])
        elif name == 'HospitalStay':
            context['doctor'] = User.objects.filter(id=context['obj']['doctor_id'])[0]
            context['room'] = Room.objects.filter(id=context['obj']['room_id'])[0]
        elif name == 'Diagnosis':
            context['patient'] = Patient.objects.filter(id=context['obj']['patient_id'])[0]
            context['doctor'] = User.objects.filter(id=context['obj']['doctor_id'])[0]
            context['diagnosiscode'] = DiagnosisCode.objects.filter(id=context['obj']['diagnosis_code_id'])[0]

        return render(request, 'main/view.html', context)

@login_required(login_url='/login')
def list(request, model_name):
    if not request.user.has_perm(f'main.view_{model_name.lower()}'):
        return redirect('home')

    obj = get_model(model_name)
    content = obj.objects.all()

    return render(request, 'main/list.html', {'content': content, 'name': model_name})

@login_required(login_url='/login')
def edit(request, model_name, id):
    if not request.user.has_perm(f'main.change_{model_name.lower()}'):
        return redirect('home')

    obj = get_object_or_404(get_model(model_name), id=id)

    if request.method == 'POST':
        form = get_form(model_name, request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(f'/view/{model_name}/{id}')
    else:
        form = get_form(model_name, instance=obj)
        return render(request, 'main/edit.html', {"form": form, "obj": obj, 'name': model_name})