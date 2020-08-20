from django.db import models

# Create your models here.

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=45)
    cedula = models.CharField(max_length=12, unique=True)
    telefono = models.CharField(max_length=45, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    correo = models.CharField(max_length=45, blank=True)
    detalles = models.CharField(max_length=200, blank=True)
    agregadoPor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' ' + self.cedula

class Cliente(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=45)
    cedula = models.CharField(max_length=12, unique=True)
    fechaInscripcion = models.DateTimeField(auto_now=True)
    fechaNacimiento = models.DateTimeField(blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    lugarTrabajo = models.CharField(max_length=45, blank=True)
    casaTel = models.CharField(max_length=45, blank=True)
    correo = models.CharField(max_length=45, blank=True)
    agregadoPor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre + ' ' + self.cedula

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    detalles = models.CharField(max_length=500, blank=True)
    agregadoPor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class LineaFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    descripcionItem = models.CharField(max_length=500, blank=True)
    cantidadItems = models.IntegerField(blank=True)
    totalItems = models.IntegerField(blank=True)
    agregadoPor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)