from django.contrib import admin
from apps.cliente.models import UserCliente, Carrito

# Register your models here.
admin.site.register(UserCliente)
admin.site.register(Carrito)
