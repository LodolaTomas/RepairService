# here is the serializer for the serviceRepairBackEnd
from rest_framework import serializers
from .models import Cliente, Tecnico, Tecnicos_Especialidad, Especialidades

## transforma de obj a json
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('cuil', 'nombre', 'apellido', 'foto')
    
class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = ('cuil', 'nombre', 'apellido', 'email', 'foto')

class EspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidades
        fields = ('nombre_especialidad',)

class Tecnicos_EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnicos_Especialidad
        fields = ('cuil_tecnico', 'especialidades_id')