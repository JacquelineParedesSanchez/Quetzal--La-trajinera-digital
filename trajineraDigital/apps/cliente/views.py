
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from apps.cliente.forms import SignUpForm, RegistroClienteForm

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
    args = {'user':request.user}
    return render(request, 'cliente/menu.html', args)


def carrito(request):
    args = {'user':request.user}
    return render(request, 'cliente/carrito.html', args)
