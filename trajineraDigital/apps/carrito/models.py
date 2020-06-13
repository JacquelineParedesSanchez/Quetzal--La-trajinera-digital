from django.conf import settings
from django.db import models
from apps.menu.models import Alimento
# Create your models here.

class Ordenar(models.Model):
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE )
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} of {self.alimento.nombre}"


class Carrito(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, blank=True, null=True)
    alimentos = models.ManyToManyField(Ordenar)
    ordenado = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username
