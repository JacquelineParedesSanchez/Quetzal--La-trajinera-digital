
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required

from apps.cliente.forms import SignUpForm, RegistroClienteForm, LoginForm
from apps.cliente.models import UserCliente

"""def login(request):
    numbers = [1,2,3,4,5]
    name= "Max Power"

    args={'myname' : name, 'numbers': numbers}
    return render(request, "cliente/home.html", args)"""

def ingreso(request):
    if request.user.is_authenticated:
        return redirect('/home/menu/')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            
            return redirect('/home/menu/')
        else: 
            return render(
                request,
                'registration/login.html',
                {'form' : form}
            )
    else:
        form = LoginForm()
        args = {'form' : form}

        return render(request, "registration/login.html", args)        

@login_required(login_url='/home/login/')
@permission_required('cliente.es_cliente', raise_exception=True)
def salir(request):
    #if request.method == 'POST':
        logout(request)

        return redirect('/home/menu/')

def registro(request):
    if request.user.is_authenticated:
        return redirect('/home/menu/')

    if request.method =='POST':
        form = SignUpForm(request.POST)
        cliente_form = RegistroClienteForm(request.POST)
        #form = UserCreationForm(request.POST)
        if form.is_valid() and cliente_form.is_valid():
            usuario = form.save()
            permiso = Permission.objects.get(name='Acceso_Cliente')
            usuario.user_permissions.add(permiso)
            cliente = cliente_form.save(commit=False)
            cliente.user = usuario

            cliente.save()

            return redirect('/home/menu/')
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

@login_required(login_url='/home/login/')
@permission_required('cliente.es_cliente', raise_exception=True)
#@permission_required('usuarios.es_administrador', raise_exception=True)
def principal(request):
    args = {'user':request.user}
    return render(request, 'cliente/principal.html', args)

@login_required(login_url='/home/login/')
@permission_required('cliente.es_cliente', raise_exception=True)
def menu(request):
    args = {'user':request.user}
    return render(request, 'cliente/menu.html', args)

@login_required(login_url='/home/login/')
@permission_required('cliente.es_cliente', raise_exception=True)
def carrito(request):
    args = {'user':request.user}
    return render(request, 'cliente/carrito.html', args)
