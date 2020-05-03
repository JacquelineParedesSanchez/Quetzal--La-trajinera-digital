from django.db import models
from apps.menu.models import * 

# Create your models here.
class Cliente(models.Model):
	
	nombre = models.CharField(max_length = 20) 
	apellidos = models.CharField(max_length = 50)
	correo = models.EmailField()
	contrasena = models.CharField(max_length = 8)
	direccion = models.TextField()
	telefono = models.CharField(max_length = 10)
	ordenes = models.ManyToManyField(Orden, blank=True)


class Repartidor(models.Model):

	nombre = models.CharField(max_length = 20) 
	apellidos = models.CharField(max_length = 50)
	correo = models.EmailField()
	contrasena = models.CharField(max_length = 8)




class Admin(models.Model):

	nombre = models.CharField(max_length = 20) 
	correo = models.EmailField()
	contrasena = models.CharField(max_length = 8)