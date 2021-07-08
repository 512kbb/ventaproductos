from django.urls import path 
from django.contrib import admin
from .views import *


urlpatterns = [

    path('', index, name="index"),
    path('contacto/', contacto, name="contacto"),
    path('feriados/', feriados, name="feriados"),
    path('registro/', registro, name="registro"),
    path('listado/', listado, name="listado"),
    path('eliminar/<id>/', eliminar, name="eliminar"),
    path('modificar/<id>/', modificar, name="modificar"),
    path('registroUsuarios/', registroUsuarios, name="registroUsuarios"),
]