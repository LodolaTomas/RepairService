from django.contrib import admin
from .models import Cliente , Tecnico , Tecnicos_Especialidad, Especialidades
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Tecnico)
admin.site.register(Tecnicos_Especialidad)
admin.site.register(Especialidades)
