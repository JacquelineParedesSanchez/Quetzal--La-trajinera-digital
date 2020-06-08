from django.contrib import admin
from .models import Carrito, Alimento, Ordenar
# Register your models here.

class CarritoAdmin(admin.ModelAdmin):
    class Meta:
        model = Carrito

admin.site.register(Carrito)
admin.site.register(Ordenar)
