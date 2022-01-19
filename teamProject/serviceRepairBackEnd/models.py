from django.db import models
from django.db.models.deletion import CASCADE
# Jerarquia BBDD
# 1-Admin
# 2-Moderador
# 3-Tecnico Listo
# 4-Empleado
# 5-Cliente Listo 

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



# Reporte de Incidentes


# Se suben las imagenes a la carpeta de upload en sus distintas categorias para ser usadas. 
# Cliente es opcional. Pero empleado y tecnico son obligatorias.

