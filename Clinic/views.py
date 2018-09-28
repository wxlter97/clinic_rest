from rest_framework import generics
from Clinic.serializers import *


class rolList(generics.ListCreateAPIView):
    queryset = rol.objects.all()
    serializer_class = rolSerializer


class rolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = rol.objects.all()
    serializer_class = rolSerializer


class usuarioList(generics.ListCreateAPIView):
    queryset = usuario.objects.all()
    serializer_class = usuarioSerializer


class usuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = usuario.objects.all()
    serializer_class = usuarioSerializer


class pacienteList(generics.ListCreateAPIView):
    queryset = paciente.objects.all()
    serializer_class = pacienteSerializer


class pacienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = paciente.objects.all()
    serializer_class = pacienteSerializer


class especialidadList(generics.ListCreateAPIView):
    queryset = especialidad.objects.all()
    serializer_class = especialidadSerializer


class especialidadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = especialidad.objects.all()
    serializer_class = especialidadSerializer


class medicoList(generics.ListCreateAPIView):
    queryset = medico.objects.all()
    serializer_class = medicoSerializer


class medicoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = medico.objects.all()
    serializer_class = medicoSerializer


class clinicaList(generics.ListCreateAPIView):
    queryset = clinica.objects.all()
    serializer_class = clinicaSerializer


class clinicaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = clinica.objects.all()
    serializer_class = clinicaSerializer


class horarioList(generics.ListCreateAPIView):
    queryset = horario.objects.all()
    serializer_class = horarioSerializer


class horarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = horario.objects.all()
    serializer_class = horarioSerializer


class scheduleList(generics.ListCreateAPIView):
    queryset = schedule.objects.all()
    serializer_class = scheduleSerializer


class scheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = schedule.objects.all()
    serializer_class = scheduleSerializer


class medicamentoList(generics.ListCreateAPIView):
    queryset = medicamento.objects.all()
    serializer_class = medicamentoSerializer


class medicamentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = medicamento.objects.all()
    serializer_class = medicamentoSerializer


class tipoProductoList(generics.ListCreateAPIView):
    queryset = tipoProducto.objects.all()
    serializer_class = tipoProductoSerializer


class tipoProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = tipoProducto.objects.all()
    serializer_class = tipoProductoSerializer


class productoList(generics.ListCreateAPIView):
    queryset = producto.objects.all()
    serializer_class = productoSerializer


class productoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = producto.objects.all()
    serializer_class = productoSerializer


class tipoEnfermedadList(generics.ListCreateAPIView):
    queryset = tipoEnfermedad.objects.all()
    serializer_class = tipoEnfermedadSerializer


class tipoEnfermedadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = tipoEnfermedad.objects.all()
    serializer_class = tipoEnfermedadSerializer


class enfermedadList(generics.ListCreateAPIView):
    queryset = enfermedad.objects.all()
    serializer_class = enfermedadSerializer


class enfermedadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = enfermedad.objects.all()
    serializer_class = enfermedadSerializer


class estadoCitaList(generics.ListCreateAPIView):
    queryset = estado_cita.objects.all()
    serializer_class = estadoCitaSerializer


class estadoCitaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = estado_cita.objects.all()
    serializer_class = estadoCitaSerializer


class citaList(generics.ListCreateAPIView):
    queryset = cita.objects.all()
    serializer_class = citaSerializer


class citaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = cita.objects.all()
    serializer_class = citaSerializer


class consultaList(generics.ListCreateAPIView):
    queryset = consulta.objects.all()
    serializer_class = consultaSerializer


class consultaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = consulta.objects.all()
    serializer_class = consultaSerializer


class recetaList(generics.ListCreateAPIView):
    queryset = receta.objects.all()
    serializer_class = recetaSerializer


class recetaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = receta.objects.all()
    serializer_class = recetaSerializer


class diagnosticoList(generics.ListCreateAPIView):
    queryset = diagnostico.objects.all()
    serializer_class = diagnosticoSerializer


class diagnosticoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = diagnostico.objects.all()
    serializer_class = diagnosticoSerializer