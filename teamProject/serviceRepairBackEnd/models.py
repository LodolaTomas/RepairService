from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
# Jerarquia BBDD
# 1-Admin
# 2-Moderador
# 3-Tecnico
# 4-Cliente listo

# Clases primarias

class Cliente(models.Model):
    cuil = models.IntegerField()
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    foto = models.CharField(max_length=45)

# Tecnico 
class Tecnico(models.Model):
    cuil = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    foto = models.CharField(max_length=45, blank=True, null=True)

class Especialidades(models.Model):
    nombre_especialidad = models.CharField(max_length=45)

class Tecnicos_Especialidad(models.Model):
   cuil_tecnico = models.ForeignKey(Tecnico, on_delete=CASCADE)
   especialidades_id = models.ManyToManyField(Especialidades)


# Hacer que se vea los datos y no object. Seguir con tecnico un poco mas. Cliente Sigue.
#06/01/2022


