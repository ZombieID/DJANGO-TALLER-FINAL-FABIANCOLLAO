from django.shortcuts import render, redirect
from miApp.forms import FormInscrito, FormInstitucion
from miApp.models import Inscritos, Institucion
from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from miApp.serialiazers import Inscritos_Serializer, Institucion_Serializer
from rest_framework.decorators import api_view
# CRUD TABLA CON FUNCIONES

def index(request):
    return render(request, 'index.html')

def listadoInscripcion(request):
    inscri = Inscritos.objects.all()
    data = {'Inscritos': inscri,'titulo':'Inscripcion'}
    return render(request, 'listarCRUD.html', data)

def eliminarInscripcion(request, id):
    inscri = Inscritos.objects.get(id = id)
    inscri.delete()
    messages.warning(request,'¡Inscripción eliminada!')
    return redirect('/inscripciones')

def agregarInscripcion(request):
    form = FormInscrito()
    titulo= 'AGREGAR INSCRIPCION'
    if request.method == 'POST':
        form = FormInscrito(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'¡Inscripcion agregada con éxito!')
        return redirect('/inscripciones')
    data = {'form' : form,'titulo':titulo}
    return render(request, 'agregar.html', data)

def actualizarInscripcion(request, id):
    inscri = Inscritos.objects.get(id = id)
    id_inscri = inscri.id
    form = FormInscrito(instance=inscri)
    titulo = 'ACTUALIZAR INSCRIPCIÓN'
    if request.method == 'POST':
        form = FormInscrito(request.POST, instance=inscri)
        if form.is_valid():
            form.save()
            messages.success(request,'¡Inscripción actualizada con éxito!')
            return redirect('/inscripciones')
    data = {'form' : form,'titulo':titulo,'id_inscri':id_inscri}
    return render(request, 'agregar.html', data)

#CLASS BASED VIEWS
    
class ListaInscritos(APIView):
    def get(self, request):
        inscri = Inscritos.objects.all()
        serial = Inscritos_Serializer(inscri, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = Inscritos_Serializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleInscritos(APIView):
    def get_object(self, pk):
        try:
            return Inscritos.objects.get(id=pk)
        except Inscritos.DoesNotExist:
            return Http404

    def get(self, request, pk):
        inscri = self.get_object(pk)
        serial = Inscritos_Serializer(inscri)
        return Response(serial.data)

    def put(self, request, pk):
        inscri = self.get_object(pk)
        serial = Inscritos_Serializer(inscri, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        inscri = self.get_object(pk)
        inscri.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    #FUNCTION BASED VIEWS INSTITUCION
    
@api_view(['GET','POST'])
def institucion_list(resquest):
    if resquest.method =='GET':
        institu = Institucion.objects.all()
        serial = Institucion_Serializer(institu, many=True)
        return Response(serial.data)
    
    if resquest.method =='POST':
        serial = Institucion_Serializer(data=resquest.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def institucion_detalle(request, id):
    try:
        institu = Institucion.objects.get(pk=id)
    except institu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serial = Institucion_Serializer(institu)
        return Response (serial.data)

    if request.method== 'PUT':
        serial = Institucion_Serializer(institu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method== 'DELETE':
        institu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def listadoInstitucion(request):
    inscri = Institucion.objects.all()
    data = {'Institu': inscri,'titulo':'Institucion'}
    return render(request, 'listarCRUD.html', data)

def eliminarInstitucion(request, id):
    inscri = Institucion.objects.get(id = id)
    inscri.delete()
    messages.warning(request,'¡Institucion eliminada!')
    return redirect('/listadoInstitucion')

def agregarInstitucion(request):
    form = FormInstitucion()
    titulo= 'AGREGAR INSTITUCION'
    if request.method == 'POST':
        form = FormInstitucion(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'¡Institucion agregada con éxito!')
        return redirect('/listadoInstitucion')
    data = {'form' : form,'titulo':titulo}
    return render(request, 'agregar.html', data)

def actualizarInstitucion(request, id):
    inscri = Institucion.objects.get(id = id)
    id_inscri = inscri.id
    form = FormInstitucion(instance=inscri)
    titulo = 'ACTUALIZAR INSTITUCION'
    if request.method == 'POST':
        form = FormInstitucion(request.POST, instance=inscri)
        if form.is_valid():
            form.save()
            messages.success(request,'¡Institucion actualizada con éxito!')
            return redirect('/listadoIntitucion')
    data = {'form' : form,'titulo':titulo,'id_inscri':id_inscri}
    return render(request, 'agregar.html', data)

