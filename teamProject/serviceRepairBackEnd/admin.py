from django.contrib import admin
from .models import Cliente , Tecnico , Tecnicos_Especialidad, Especialidades, Empleado
from .models import Room, Message
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Tecnico)
admin.site.register(Tecnicos_Especialidad)
admin.site.register(Especialidades)
admin.site.register(Empleado)
admin.site.register(Room)
admin.site.register(Message)