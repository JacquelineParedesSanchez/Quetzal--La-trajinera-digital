from django.contrib import admin
from apps.usuarios.models import Admin, Repartidor

# Register your models here.
admin.site.register(Admin)
admin.site.register(Repartidor)
#admin.site.register(Cliente)