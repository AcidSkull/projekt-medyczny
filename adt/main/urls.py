from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('create/<str:model_name>', views.create, name='create'),
    path('view/<str:model_name>/<int:id>', views.view, name='view'),
    path('edit/<str:model_name>/<int:id>', views.edit, name='edit'),
]