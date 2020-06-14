from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
"""class Repartidor(models.Model):

	nombre = models.CharField(max_length = 20) 
	apellidos = models.CharField(max_length = 50)
	correo = models.EmailField()
	contrasena = models.CharField(max_length = 8)
	
	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellidos)"""

"""class Administrador(models.Model):

	nombre_usuario = models.CharField(max_length = 20) 
	correo = models.EmailField(null=True)
	contrasena = models.CharField(max_length = 8)

	def __str__(self):
		return '{}'.format(self.nombre_usuario)"""

"""class User(AbstractUser):
	es_cliente = models.BooleanField(default=False)
	es_repartidor = models.BooleanField(default=False)
	es_administrador = models.BooleanField(default=False)"""
	
		


class Repartidor(models.Model):

	user = models.OneToOneField(
		User, related_name="repartidor", on_delete=models.CASCADE, blank=True, null=True
	)
	tel = RegexValidator(r'^(55)\d{8}', "El número debe estár en formato LADA.")
	telefono = models.CharField(validators=[tel], max_length=10, blank=True, null=True)
	
	class Meta:
		#proxy = True
		permissions = [('es_repartidor', "Acceso_Repartidor")]

	def __str__(self):
		return '{} {} {}'.format(self.user.first_name, self.user.last_name, self.id)

	def __repr__(self):
		return self.__str__()

class Administrador(models.Model):
	user = models.OneToOneField(
		User, related_name="administrador", on_delete=models.CASCADE, blank=True, null=True
	)

	class Meta:
		#proxy = True
		permissions = [('es_administrador', "Acceso_Administrador")]

	def __str__(self):
		return '{} {}'.format(self.user.first_name, self.user.last_name)

	def __repr__(self):
		return self.__str__()