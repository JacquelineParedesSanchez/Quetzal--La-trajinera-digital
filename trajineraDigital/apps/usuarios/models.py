from django.db import models

# Create your models here.
class Repartidor(models.Model):
	nombre = models.CharField(max_length = 20) 
	apellidos = models.CharField(max_length = 50)
	correo = models.EmailField()
	contrasena = models.CharField(max_length = 8)
	
	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellidos)

class Admin(models.Model):
	nombre_usuario = models.CharField(max_length = 20) 
	correo = models.EmailField()
	contrasena = models.CharField(max_length = 8)

	def __str__(self):
		return '{}'.format(self.nombre_usuario)