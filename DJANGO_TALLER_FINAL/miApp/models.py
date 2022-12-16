import datetime
from django.db import models

# Create your models here.

estado_choices =(
    ("RESERVADO","RESERVADO"),
    ("COMPLETADA","COMPLETADA"),
    ("ANULADA","ANULADA"),
    ("NO ASISTEN","NO ASISTEN"),
)

class Inscritos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre =models.CharField(blank=False,max_length=50)
    fono =models.CharField(max_length=15,blank=False,verbose_name="Teléfono")
    fecha_insc =models.DateField(blank=False,verbose_name="Fecha de Inscripción")
    hora_insc =models.TimeField(blank=False,verbose_name="Hora de Inscripción")
    institucion =models.CharField(blank=False,max_length=20)
    estado = models.CharField(max_length=10,choices=estado_choices,blank=False,default="RESERVADO")
    observacion =models.CharField(blank=True, max_length=150)

class Institucion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre =models.CharField(blank=False,max_length=20)
    region =models.CharField(blank=False,max_length=20)
    ciudad =models.CharField(blank=False,max_length=20)
