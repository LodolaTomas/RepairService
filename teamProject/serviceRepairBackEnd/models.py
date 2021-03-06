from re import T
from this import d
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.conf import settings


# imports



# Tecnico 
class Tecnico(models.Model):
    cuil = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='imagesTecnico')
    # Muestra Nombre Apellido y Cuil
    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.cuil}'

class Especialidades(models.Model):
    nombre_especialidad = models.CharField(max_length=45)

    def  __str__(self):
        return f'{self.nombre_especialidad}'

class Tecnicos_Especialidad(models.Model):
   cuil_tecnico = models.ForeignKey(Tecnico, on_delete=CASCADE)
   especialidades_id = models.ManyToManyField(Especialidades)   


   def __str__(self): 
       valores = list(self.especialidades_id.values())
       especialidades = ""
       tecnico = str(self.cuil_tecnico)

       for valor in valores:
           especialidades += valor["nombre_especialidad"] + " "
                   
       return tecnico + " - " + especialidades

# Empleado
class Empleado(models.Model):
    cuil = models.IntegerField()
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    image = models.ImageField(upload_to='imagesEmpleado')
    roll = models.IntegerField()

# Cliente
class Cliente(models.Model):
    cuil = models.IntegerField()
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    image = models.ImageField(upload_to='imagesCliente', blank = True)

    def __str__(self):
        nombre = self.nombre
        apellido = self.apellido
        cuil = str(self.cuil)

        return nombre + " " + apellido + " - " + cuil

class Room(models.Model):
    host = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    #topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Message(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # Si se borra el Room se deletean los mensajes.
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]


