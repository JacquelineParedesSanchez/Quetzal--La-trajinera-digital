
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required

from apps.cliente.forms import SignUpForm, RegistroClienteForm, LoginForm
from apps.cliente.models import UserCliente, Carrito
from apps.menu.models import Categoria, Alimento

from decimal import Decimal
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
    categoria = Categoria.objects.all()
    args = {'user':request.user, 'Categoria': categoria}
    return render(request, 'cliente/menu.html', args)

@login_required(login_url='/home/login/')
@permission_required('cliente.es_cliente', raise_exception=True)
def carrito(request):
    try:
        id_carro = request.session['carro_id']
    except:
        id_carro = None

    if id_carro:
        carro = Carrito.objects.get(id=id_carro)
        contexto = {'carro' : carro}
    else:
        mensaje = "Tu carro está vacío."
        contexto = {'vacio' : True, 'mensaje' : mensaje}

    return render(request, 'cliente/carrito.html', contexto)

def agrega_carrito(request, pk):
    try:
        id_carro = request.session['carro_id']
    except:
        carro_nuevo = Carrito()
        carro_nuevo.save()
        request.session['carro_id'] = carro_nuevo.id
        id_carro = carro_nuevo.id

    carro = Carrito.objects.get(id=id_carro)

    #try:
    alim = Alimento.objects.get(id=pk)
    #except:
        #pass

    if not alim in carro.alimentos.all():
        carro.alimentos.add(alim)
    else:
        carro.alimentos.remove(alim)

    temp_total = Decimal(0.00)
    for producto in carro.alimentos.all():
        temp_total += producto.precio

    carro.total = temp_total
    carro.save()

    return redirect('/home/carrito/')

@login_required(login_url='/home/login/')
@permission_required('cliente.es_cliente', raise_exception=True)
def ver_menu(request,pk):
    categoria = Categoria.objects.get(id=pk)
    alimentos = Alimento.objects.filter(categoria = categoria)
    contexto = {'Categoria': categoria, 'Alimentos': alimentos }
    return render(request, 'cliente/ver_carta.html', contexto)