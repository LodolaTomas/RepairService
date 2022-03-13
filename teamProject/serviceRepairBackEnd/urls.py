# Forma recomendada en la que puedo crear un archivo en mi api para poder usarlo en mi app
from django.urls import path # Para incluir las urls de otras apps
from . import views


urlpatterns = [
    path('cliente', views.client_api, name='clients_api'),
    path('tecnico', views.tecnico_api, name = 'tecnico_api'),
    path('cliente/<int:cuil>/', views.client_detail, name='client_detail'),
]