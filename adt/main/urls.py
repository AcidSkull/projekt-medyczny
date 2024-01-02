from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('create_patient', views.create_patient, name='create_patient'),
    path('create_appointment', views.create_appointment, name='create_appointment'),
    path('patient/<int:id>', views.patient, name='patient'),
]