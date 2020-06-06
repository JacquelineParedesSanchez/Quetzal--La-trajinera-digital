from django.contrib import admin
from .models import Carrito
# Register your models here.

class CarritoAdmin(admin.ModelAdmin):
    class Meta:
        model = Carrito

admin.site.register(Carrito,CarritoAdmin)
