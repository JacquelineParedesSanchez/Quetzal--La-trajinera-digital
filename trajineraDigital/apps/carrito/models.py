from django.conf import settings
from django.db import models
from apps.menu.models import Alimento
# Create your models here.

class Carrito(models.Model):
    alimentos = models.ManyToManyField(Alimento, null=True, blank=True)
    precio = models.DecimalField(max_digits=100, decimal_places=2, default= 0.00)

    def __str__(self):
        return self.user.username

class Ordenar(models.Model):
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
