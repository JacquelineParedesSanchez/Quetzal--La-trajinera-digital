
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required

from apps.cliente.forms import SignUpForm, RegistroClienteForm, LoginForm
from apps.cliente.models import UserCliente, Carrito
from apps.menu.models import Categoria, Alimento, Orden

from decimal import Decimal


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
        try:
            id_carro = request.session['carro_id']
        except:
            id_carro = None
        print(id_carro)
        if id_carro:
            carro = Carrito.objects.get(id=id_carro)
            carro.delete()

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
def ver_menu(request,pk):
    categoria = Categoria.objects.get(id=pk)
    alimentos = Alimento.objects.filter(categoria = categoria)

    try:
        id_carro = request.session['carro_id']
    except:
        id_carro = None

    if id_carro:
        carro = Carrito.objects.get(id=id_carro)
        contexto = {
            'Categoria': categoria, 
            'Alimentos': alimentos, 
            'carro_alimentos' : carro.alimentos.all()
        }
    else:        
        contexto = {'Categoria': categoria, 'Alimentos': alimentos }

    return render(request, 'cliente/ver_carta.html', contexto)

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

@login_required(login_url='/home/login/')
@permission_required('cliente.es_cliente', raise_exception=True)
def agrega_carrito(request, pk):
    try:
        id_carro = request.session['carro_id']
    except:
        carro_nuevo = Carrito()
        carro_nuevo.save()
        request.session['carro_id'] = carro_nuevo.id
        id_carro = carro_nuevo.id

    carro = Carrito.objects.get(id=id_carro)
    alim = Alimento.objects.get(id=pk)

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
def registra_orden(request):
    try:
        id_carro = request.session['carro_id']
    except:
        id_carro = None

    if id_carro:
        carro = Carrito.objects.get(id=id_carro)
        user_actual = request.user
        cliente_actual = UserCliente.objects.get(user=user_actual)
        orden = Orden(
            fecha_orden=timezone.now(),
            orden=cliente_actual,
            precio_total=carro.total
        )
        orden.save()

        for alim in carro.alimentos.all():
            orden.alimentos_orden.add(alim)
            carro.alimentos.remove(alim)

        carro.total = 0.00
        carro.save()

    return render(request, 'cliente/orden.html', {'user':request.user})

@login_required(login_url='/home/login/')
@permission_required('cliente.es_cliente', raise_exception=True)
def ver_ordenes(request):
    cliente_actual = UserCliente.objects.get(user=request.user)
    orders = Orden.objects.filter(orden=cliente_actual)

    if orders:
        contexto = {'ordenes' : orders}
    else:
        mensaje = "No tienes ordenes registradas."
        contexto = {'vacio' : True, 'mensaje' : mensaje}

    return render(request, 'cliente/ordenes.html', contexto)

@login_required(login_url='/home/login/')
@permission_required('cliente.es_cliente', raise_exception=True)
def orden_alimentos(request,pk):
    orden = Orden.objects.get(id=pk)
    alimentos = orden.alimentos_orden.all()
    contexto = {'orden': alimentos}
    return render(request, 'cliente/alimentos_orden.html', contexto)

@login_required(login_url='/home/login/')
@permission_required('cliente.es_cliente', raise_exception=True)
def cuenta(request):
    cliente_actual = UserCliente.objects.get(user=request.user)
    return render(request, 'cliente/cuenta.html', {'cliente' : cliente_actual})

@login_required(login_url='/home/login/')
@permission_required('cliente.es_cliente', raise_exception=True)
def cambiar_info(request):
    cliente_form = RegistroClienteForm(request.POST)
    #form = UserCreationForm(request.POST)
    if cliente_form.is_valid():
        #cliente = cliente_form.save(commit=False)
        cliente = UserCliente.objects.get(user=request.user)
        cliente.direccion = cliente_form.cleaned_data['direccion']
        cliente.telefono = cliente_form.cleaned_data['telefono']

        cliente.save()

        return redirect('/home/cuenta/')
    else:
        return render(
            request, 
            'cliente/cambiar_info.html', 
            {'cliente_form' : cliente_form}
        )
