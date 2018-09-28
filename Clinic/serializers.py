from rest_framework import serializers
from Clinic.models import *


class rolSerializer(serializers.ModelSerializer):
    class Meta:
        model = rol
        fields = '__all__'


class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = '__all__'


class pacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = paciente
        fields = '__all__'


class especialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = especialidad
        fields = '__all__'


class medicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = medico
        fields = '__all__'


class clinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = clinica
        fields = '__all__'


class horarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = horario
        fields = '__all__'


class scheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = schedule
        fields = '__all__'


class medicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = medicamento
        fields = '__all__'


class tipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoProducto
        fields = '__all__'


class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = '__all__'


class tipoEnfermedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoEnfermedad
        fields = '__all__'


class enfermedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = enfermedad
        fields = '__all__'


class estadoCitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = estado_cita
        fields = '__all__'


class citaSerializer(serializers.ModelSerializer):
    class Meta:
        model = cita
        fields = '__all__'


class consultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = consulta
        fields = '__all__'


class recetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = receta
        fields = '__all__'


class diagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = diagnostico
        fields = '__all__'