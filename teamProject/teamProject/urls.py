from django.contrib import admin
from django.urls import path, include # Para incluir las urls de otras apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('serviceRepairBackEnd.urls')) # Para incluir las urls de otras apps
]
