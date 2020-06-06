from django.shortcuts import render

# Create your views here.
from .models import Carrito

def view(request):
    carrito = Carrito.objects.all()
    args={'Carrito':carrito}
    return render(request, "carrito/carrito.html", args)
