from __future__ import unicode_literals

from django.db import models
#-*- coding: utf-8 -*-  
from django.utils import timezone
from django.db import models
from django.conf import settings

import logging  
logger = logging.getLogger(__name__)



class Lugar(models.Model): 
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200) 

    def __str__(self):
        return self.nombre

    
class Usuario(models.Model): 
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    dni = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.nombre


class Item(models.Model): 
    nombre = models.CharField(max_length=50) 

    def __str__(self):
        return self.nombre


class Donativo(models.Model): 
    direccion = models.CharField(max_length=50)
    geo_ubicacion = models.CharField(max_length=50) 
    usuario = models.ForeignKey(Usuario, null=True, blank=True)
    lugar = models.ForeignKey(Lugar, null=True, blank=True)

    def __str__(self):
        return "HECHO POR :  " + str(self.usuario.nombre) + str(" ::: Direccion usuario: ") + str(self.direccion) 


class DonativoDetalle(models.Model):  
    cantidad = models.IntegerField(default=0) 
    item = models.ForeignKey(Item, null=True, blank=True)
    donativo = models.ForeignKey(Donativo, null=True, blank=True)

    def __str__(self):
        return self.item.nombre + "("+ str(self.cantidad) +" UNIDADES) "

 

