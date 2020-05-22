from datetime import datetime

from django.db import models

# Create your models here.

class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    lunes_entrada = models.TimeField(blank=True, null=True)
    lunes_salida = models.TimeField(blank=True, null=True)

    martes_entrada = models.TimeField(blank=True, null=True)
    martes_salida = models.TimeField(blank=True, null=True)

    miercoles_entrada = models.TimeField(blank=True, null=True)
    miercoles_salida = models.TimeField(blank=True, null=True)

    jueves_entrada = models.TimeField(blank=True, null=True)
    jueves_salida = models.TimeField(blank=True, null=True)

    viernes_entrada = models.TimeField(blank=True, null=True)
    viernes_salida = models.TimeField(blank=True, null=True)

    sabado_entrada = models.TimeField(blank=True, null=True)
    sabado_salida = models.TimeField(blank=True, null=True)

    domingo_entrada = models.TimeField(blank=True, null=True)
    domingo_salida = models.TimeField(blank=True, null=True)

    fecha = models.DateTimeField(default=datetime.now(), editable=False)


    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.fecha = datetime.now()
        super().save(*args, **kwargs)

class Colaborador(models.Model):
    PISOS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )

    cedula = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=45)
    correo = models.EmailField()
    activo = models.BooleanField(default=False)
    correo_jefe = models.EmailField()
    piso = models.CharField(max_length=1, choices=PISOS)
    saludable = models.BooleanField(default=False, editable=False)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)

    fecha = models.DateTimeField(default=datetime.now(), editable=False)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.fecha = datetime.now()
        super().save(*args, **kwargs)

class Evaluacion(models.Model):
    colaborador = models.OneToOneField(Colaborador, on_delete=models.CASCADE)
    observacion = models.TextField()
    saludable = models.BooleanField()
    nombre = models.CharField(max_length=45, editable=False)
    cedula = models.CharField(max_length=45, editable=False)
    fecha = models.DateTimeField(default=datetime.now(), editable=False)

    def __str__(self):
        return self.colaborador.nombre

    def save(self, *args, **kwargs):
        self.fecha = datetime.now()
        self.colaborador.saludable = self.saludable
        self.nombre = self.colaborador.nombre
        self.cedula = self.colaborador.cedula
        self.colaborador.save()
        super().save(*args, **kwargs)

class Ingreso(models.Model):
    ACCIONES = (
        ('in', 'in'),
        ('out', 'out'),
    )
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=datetime.now())
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    temperatura = models.FloatField()
    permitido = models.BooleanField()
    observacion = models.CharField(max_length=100)
    accion = models.CharField(max_length=3, choices=ACCIONES)
    nombre = models.CharField(max_length=45, editable=False)
    cedula = models.CharField(max_length=10, editable=False)

    def __str__(self):
        return self.colaborador.nombre

    def save(self, *args, **kwargs):
        self.nombre = self.colaborador.nombre
        self.cedula = self.colaborador.cedula
        super().save(*args, **kwargs)

