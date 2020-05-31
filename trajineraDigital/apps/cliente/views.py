
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
<<<<<<< HEAD
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
=======
from apps.cliente.forms import SignUpForm
>>>>>>> dc77e66107d6c112514540cecbad1ffda0f3d02c

#from users.

# Create your views here.
#class SignUpView(View):

def login(request):
    numbers = [1,2,3,4,5]
    name= "Max Power"

    args={'myname' : name, 'numbers': numbers}
    return render(request, "cliente/home.html", args)


def registro(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')
        else:
            print(form.errors)
    else:
        form=SignUpForm()

        args = {'form': form}
        return render(request, 'registration/register.html', args)

@login_required
def principal(request):
    args = {'user':request.user}
    return render(request, 'cliente/principal.html', args)

@login_required
def menu(request):
    args = {'user':request.user}
    return render(request, 'cliente/menu.html', args)

@login_required
def carrito(request):
    args = {'user':request.user}
    return render(request, 'cliente/carrito.html', args)
