from django.contrib import admin
from apps.usuarios.models import Administrador, Repartidor

# Register your models here.
admin.site.register(Administrador)
admin.site.register(Repartidor)
#admin.site.register(Cliente)