from django.db import models


class rol(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    nivel = models.IntegerField()


class usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    apellido = models.TextField()
    telefono = models.TextField()
    dui = models.TextField()
    id_rol = models.ForeignKey(rol, on_delete=models.CASCADE)


class paciente(models.Model):
    id = models.AutoField(primary_key=True)
    dui = models.CharField(max_length=10)
    nombre = models.TextField()
    apellido = models.TextField()
    f_nac = models.DateField()
    telefono = models.CharField(max_length=15)
    sexo = models.CharField(max_length=1)
    foto = models.ImageField(default='fotos/None/noimg.png')

class especialidad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()


class medico(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    jvpm = models.CharField(max_length=10)
    id_especialidad = models.ForeignKey(especialidad, on_delete=models.CASCADE)


class clinica(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    ubicacion = models.TextField()
    numero_plazas = models.IntegerField()


class horario(models.Model):
    id = models.AutoField(primary_key=True)
    inicio = models.TimeField()
    fin = models.TimeField()
    cupos = models.IntegerField()


class schedule(models.Model):
    id = models.AutoField(primary_key=True)
    dia = models.CharField(max_length=1)
    id_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    id_horario = models.ForeignKey(horario, on_delete=models.CASCADE)
    id_clinica = models.ForeignKey(clinica, on_delete=models.CASCADE)


class medicamento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    composicion = models.TextField()
    observaciones = models.TextField()


class tipoProducto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    descripcion = models.TextField()


class producto(models.Model):
    id = models.AutoField(primary_key=True)
    id_medicamento = models.ForeignKey(medicamento, models.CASCADE)
    nombre = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)
    id_tipoProducto = models.ForeignKey(tipoProducto, on_delete=models.CASCADE)


class tipoEnfermedad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()


class enfermedad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    id_tipoEnfermedad = models.ForeignKey(tipoEnfermedad, models.CASCADE)
    sintomas = models.TextField()


class estado_cita(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()


class cita(models.Model):
    id = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    id_schedule = models.ForeignKey(schedule, on_delete=models.CASCADE)
    fecha_realizacion = models.DateTimeField()
    fecha_cita = models.DateField
    observaciones = models.TextField()
    id_estado = models.ForeignKey(estado_cita, on_delete=models.CASCADE)


class consulta(models.Model):
    id = models.AutoField(primary_key=True)
    id_cita = models.ForeignKey(cita, on_delete=models.CASCADE)
    peso = models.IntegerField()
    altura = models.IntegerField()
    presion_arterial = models.CharField(max_length=8)
    temperatura = models.CharField(max_length=10)
    obervaciones = models.TextField


class receta(models.Model):
    id = models.AutoField(primary_key=True)
    id_consulta = models.ForeignKey(consulta, on_delete=models.CASCADE)
    via_administracion = models.CharField(max_length=50)
    id_producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    posologia = models.TextField()
    fecha = models.DateTimeField()


class diagnostico(models.Model):
    id = models.AutoField(primary_key=True)
    id_consulta = models.ForeignKey(consulta, on_delete=models.CASCADE)
    id_enfermedad = models.ForeignKey(enfermedad, on_delete=models.CASCADE)