from django.db import models
from django.contrib.auth.models import User

from apps.menu.models import Orden
# Create your models here.
class Cliente(models.Model):
	
	user = models.OneToOneField(
		User, related_name="client", on_delete=models.CASCADE
	)
	direccion = models.TextField()
	telefono = models.CharField(max_length=10)
	ordenes = models.ManyToOneField(Orden, blank=True)

	def __str__(self):
		return f"Usuario({self.user.id} {self.user.first_name}
			{self.user.last_name} {self.user.email})"

	def __repr__(self):
		return self.__str__()