from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from apps.menu.models import Alimento
# Create your views here.
from .models import Carrito, Alimento


#lista de compras
def lista(request):
    args={'alimentos': Alimento.objects.all()}
    return render(request, "cliente/menu.html", args)
