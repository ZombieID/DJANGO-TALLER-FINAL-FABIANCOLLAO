"""DJANGO_TALLER_FINAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('inscripciones/', views.listadoInscripcion),
    path('eliminarInscripcion/<int:id>', views.eliminarInscripcion),
    path('agregarInscripcion/', views.agregarInscripcion),
    path('actualizarInscripcion/<int:id>', views.actualizarInscripcion),
    #CLASE BASED VIEWS
    path('cbw_inscripciones/', views.ListaInscritos.as_view()),
    path('cbw_detalle_inscripciones/<int:pk>', views.DetalleInscritos.as_view()),
    #FUNCTION BASED VIEWS
    path('fbw_listaInstitucion/',views.institucion_list),
    path('fbw_detalleInstitucion/<int:id>', views.institucion_detalle),
    #CRUD INSTITUCION
    path('listadoInstitucion/', views.listadoInstitucion),
    path('eliminarInstitucion/<int:id>', views.eliminarInstitucion),
    path('agregarInstitucion/', views.agregarInstitucion),
    path('actualizarInstitucion/<int:id>', views.actualizarInstitucion),
]
