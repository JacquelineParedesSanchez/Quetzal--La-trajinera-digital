from django.conf import settings
from django.db import models
from apps.menu.models import Alimento
# Create your models here.

class Carrito(models.Model):
    alimentos = models.ManyToManyField(Alimento, null=True, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default= 0.00)
    ordenado = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Ordenar(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, blank=True, null=True)
    ordenado = models.BooleanField(default=False)
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} of {self.alimento.nombre}"
