
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from apps.menu.models import Alimento
from apps.carrito.models import Carrito, Ordenar
from apps.cliente.forms import SignUpForm, RegistroClienteForm
from django.contrib.auth.decorators import login_required

def login(request):
    numbers = [1,2,3,4,5]
    name= "Max Power"

    args={'myname' : name, 'numbers': numbers}
    return render(request, "cliente/home.html", args)


def registro(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        cliente_form = RegistroClienteForm(request.POST)
        #form = UserCreationForm(request.POST)
        if form.is_valid() and cliente_form.is_valid():
            usuario = form.save()
            cliente = cliente_form.save(commit=False)
            cliente.user = usuario

            cliente.save()

            return redirect('/home')
        else:
            return render(
                request,
                'registration/register.html',
                {'form' : form, 'cliente_form' : cliente_form}
            )

    else:
        form = SignUpForm()
        cliente_form = RegistroClienteForm()
        #form=UserCreationForm()

        args = {'form': form, 'cliente_form' : cliente_form}
        return render(request, 'registration/register.html', args)


def principal(request):
    args = {'user':request.user}
    return render(request, 'cliente/principal.html', args)

def menu(request):
    args={'alimentos': Alimento.objects.all()}
    return render(request, "cliente/menu.html", args)

@login_required
def carrito(request):
    args={'orden': Orden.objects.all()}
    return render(request, "cliente/carrito.html", args)
@login_required
def agregar_carrito(request, nombre):
    alimento = get_object_or_404(Alimento, nombre=nombre)
    ordenar, created= Ordenar.objects.get_or_create(alimento=alimento, user=request.user, ordenado=False)
    carrito_qs = Carrito.objects.filter(user=request.user, ordenado=False)
    if carrito_qs.exists():
        carrito = carrito_qs[0]
        if carrito.alimentos.filter(nombre=alimento.nombre).exists():
            ordenar.cantidad +=1
            ordenar.save()
        else:
            messages.info(request,"Se ha añadido este objeto al carrito")
            carrito.alimento.add(ordenar)
    else:
        carrito = Carrito.objects.create(user=request.user)
        carrito.alimentos.add(ordenar)
        messages.info(request,"Se ha añadido este objeto al carrito")
    return redirect("menu",nombre= nombre)
@login_required
def quitar_carrito(request, nombre):
    alimento = get_object_or_404(Alimento, nombre=nombre)
    carrito_qs = Carrito.objects.filter(user=request.user, ordenado=False)
    if carrito_qs.exists():
        carrito = carrito_qs[0]
        if carrito.alimentos.filter(nombre=alimento.nombre).exists():
            ordenar = Ordenar.objects.filter(alimento=alimento, user=request.user, ordenado=False)[0]
            if ordenar.cantidad > 1:
                ordenar.cantidad -=1

                ordenar.save()
            else:
                ordenar.delete()
            messages.info(request,"Se quitado este objeto al carrito")
            return redirect("menu",nombre= nombre)
        else:
            messages.info(request,"Este objeto no estaba en tu carrito")
            return redirect("menu",nombre= nombre)
    else:
        messages.info(request,"No tienes una orden")
        return redirect("menu",nombre= nombre)
