from django.db import models
from apps.menu.models import Alimento
# Create your models here.

class Carrito(models.Model):
    alimentos = models.ManyToManyField(Alimento, null=True, blank=True)
    precio = models.DecimalField(max_digits=100, decimal_places=2, default= 0.00)

    def __unicode__(self):
        return "Cart id: %s" %(self.id)
