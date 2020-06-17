from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.dispatch import receiver

from apps import menu as menu

class UserCliente(models.Model):

	user = models.OneToOneField(
		User, related_name="client", on_delete=models.CASCADE
	)
	direccion = models.TextField(blank=False)
	tel = RegexValidator(r'^(55)\d{8}', "El número debe estár en formato LADA.")
	telefono = models.CharField(validators=[tel], max_length=10, blank=False)
	
	class Meta:
		#proxy = True
		permissions = [('es_cliente', "Acceso_Cliente")]

	def __str__(self):
		return "{}, {}, {}, {}, {}".format(
			self.user.username,
			self.user.first_name, 
			self.user.last_name, 
			self.user.email, 
			self.telefono,
		)

	def __repr__(self):
		return self.__str__()


class Carrito(models.Model):
	#cliente = models.ForeignKey(User, null=True, blank=True)
	alimentos = models.ManyToManyField('menu.Alimento', blank=True)
	total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

	def __str__(self):
		return "Carrito: {}".format(
			self.id,
			#self.cliente.username,
			#self.cliente.email
		)

	def __repr__(self):
		return self.__str__()

"""def create_profile(sender,**kwargs):
	if kwargs['created']:
		client_profile=UserCliente.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)"""
