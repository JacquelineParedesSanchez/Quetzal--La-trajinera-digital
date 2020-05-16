from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from apps.menu.models import Orden
# Create your models here.
class UserCliente(models.Model):

	user = models.OneToOneField(
		User, related_name="client", on_delete=models.CASCADE
	)
	direccion = models.TextField(default='')
	telefono = models.IntegerField(default=0)
#	ordenes = models.ManyToOneField(Orden, blank=True)

#	def __str__(self):
#		return f"Usuario({self.user.id} {self.user.first_name}
#			{self.user.last_name} {self.user.email})"

def create_profile(sender,**kwargs):
	if kwargs['created']:
		client_profile=UserCliente.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

#	def __repr__(self):
#		return self.__str__()
