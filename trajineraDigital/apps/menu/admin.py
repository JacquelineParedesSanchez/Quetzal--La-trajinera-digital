from django.contrib import admin
from apps.menu.models import Alimento, Categoria, Estado, Orden

# Register your models here.
admin.site.register(Alimento)
admin.site.register(Categoria)
admin.site.register(Estado)
admin.site.register(Orden)