from dataclasses import fields
import datetime
from importlib.abc import ExecutionLoader
from pyexpat import model
from tabnanny import verbose
from django import forms
from django.forms import ValidationError
from miApp.models import Inscritos, Institucion
from miApp import models

class FormInscrito(forms.ModelForm):
    nombre = forms.CharField(label="Nombre",max_length=50,required=True)
    fono = forms.CharField(max_length=20,required=True)
    fecha_insc = forms.DateField(required=True)#initial=datetime.datetime.now(),disabled=True)
    hora_insc = forms.TimeField(required=True)# initial=datetime.datetime.now(),disabled=True)
    institucion= forms.CharField(required=True)
    estado = forms.CharField(widget=forms.Select(choices=models.estado_choices))
    observacion = forms.CharField(max_length=150,required=False)

    class Meta:
        model = Inscritos
        fields = ('__all__')
    

class FormInstitucion(forms.ModelForm):
    nombre = forms.CharField(max_length=20)
    region =forms.CharField(max_length=20)
    ciudad =forms.CharField(max_length=20)
    class Meta:
        model = Institucion
        fields = ("__all__")

