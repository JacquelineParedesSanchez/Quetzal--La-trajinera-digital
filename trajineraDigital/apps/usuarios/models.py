from django.db import models
from apps.menu.models import * 

# Create your models here.
class Repartidor(models.Model):

	nombre = models.CharField(max_length = 20) 
	apellidos = models.CharField(max_length = 50)
	correo = models.EmailField()
	contrasena = models.CharField(max_length = 8)




class Admin(models.Model):

	nombre = models.CharField(max_length = 20) 
	correo = models.EmailField()
	contrasena = models.CharField(max_length = 8)