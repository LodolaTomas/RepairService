# Forma recomendada en la que puedo crear un archivo en mi api para poder usarlo en mi app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.cliente_list, name='cliente_list'),
]
