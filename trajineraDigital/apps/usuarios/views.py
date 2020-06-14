from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponse 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Permission
from apps.menu.models import Alimento, Categoria, Orden, Estado
from apps.usuarios.models import Administrador, Repartidor
from django.contrib.auth.models import User
from apps.usuarios.forms import AlimentoForm, CategoriaForm, RepartidorForm, OrdenesForm, IngresoForm, TelefonoForm
from trajineraDigital.settings import EMAIL_HOST_USER

# Create your views here.
@login_required(login_url='/administrador/ingreso/')
@permission_required('usuarios.es_administrador', raise_exception=True)
def indexAdministrador(request):
    return render(request,'admin/index_admin.html')

#@permission_required('usuarios.es_administrador', raise_exception=True)
def ingreso(request):
    if request.user.is_authenticated:
        return redirect('/administrador/index_administrador')

    if request.method == 'POST':
        form = IngresoForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)

            return redirect('/administrador/index_administrador/')
        else:

            return render(
                request,
                'autenticacion/login.html',
                {'form' : form}
            )
    else:
        form = IngresoForm()
        args = {'form' : form}

        return render(request, "autenticacion/login.html", args)  

@login_required(login_url='/administrador/ingreso/')
@permission_required('usuarios.es_administrador', raise_exception=True)
def salir(request):
    logout(request)

    return redirect('/administrador/ingreso/')   


class menu_Alimentos_Administrador(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url='/administrador/ingreso/'
    redirect_field_name = 'redirect_to'
    permission_required = 'usuarios.es_administrador'

    model = Alimento
    template_name = 'admin/alimento/alimento.html'

class menu_Alimentos_Editar(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url='/administrador/ingreso/'
    redirect_field_name = 'redirect_to'
    permission_required = 'usuarios.es_administrador'

    model = Alimento
    template_name = 'admin/alimento/menu_editar_alimento.html'

class menu_Alimentos_Eliminar(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url='/administrador/ingreso/'
    redirect_field_name = 'redirect_to'
    permission_required = 'usuarios.es_administrador'

    model = Alimento
    template_name = 'admin/alimento/menu_eliminar_alimento.html'


class Crear_Alimento(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url='/administrador/ingreso/'
    redirect_field_name = 'redirect_to'
    permission_required = 'usuarios.es_administrador'

    model = Alimento
    form_class = AlimentoForm
    template_name = 'admin/alimento/crear_alimento.html'
    success_url = reverse_lazy('menu_alimentos')

class Editar_Alimento(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url='/administrador/ingreso/'
    redirect_field_name = 'redirect_to'
    permission_required = 'usuarios.es_administrador'

    model = Alimento
    form_class = AlimentoForm
    template_name = 'admin/alimento/editar_alimento.html'
    success_url = reverse_lazy('menu_alimentos')

class Eliminar_Alimento(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url='/administrador/ingreso/'
    redirect_field_name = 'redirect_to'
    permission_required = 'usuarios.es_administrador'

    model = Alimento
    form_class = AlimentoForm
    template_name = 'admin/alimento/eliminar_alimento.html'
    success_url = reverse_lazy('menu_alimentos')




class menu_Categoria(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url='/administrador/ingreso/'
    redirect_field_name = 'redirect_to'
    permission_required = 'usuarios.es_administrador'

    model = Categoria
    template_name = 'admin/categoria/categorias.html'

@login_required(login_url='/administrador/ingreso/')
@permission_required('usuarios.es_administrador', raise_exception=True)
def menu_Categoria_Alimentos(request, categoria):
    alimento = Alimento.objects.all()
    contexto = {'alimentos': alimento, 'Categoria': categoria }
    return render(request, 'admin/categoria/alimentos_categoria.html', contexto) 


class menu_Editar_Categoria(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url='/administrador/ingreso/'
    redirect_field_name = 'redirect_to'
    permission_required = 'usuarios.es_administrador'

    model = Categoria
    template_name = 'admin/categoria/menu_editar_categoria.html'

class menu_Eliminar_Categoria(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url='/administrador/ingreso/'
    redirect_field_name = 'redirect_to'
    permission_required = 'usuarios.es_administrador'

    model = Categoria
    template_name = 'admin/categoria/menu_eliminar_categoria.html'


class Crear_Categoria(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url='/administrador/ingreso/'
    redirect_field_name = 'redirect_to'
    permission_required = 'usuarios.es_administrador'

    model = Categoria
    form_class = CategoriaForm
    template_name = 'admin/categoria/crear_categoria.html'
    success_url = reverse_lazy('listado_categorias')

class Editar_Categoria(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url='/administrador/ingreso/'
    redirect_field_name = 'redirect_to'
    permission_required = 'usuarios.es_administrador'

    model = Categoria
    form_class = CategoriaForm
    template_name = 'admin/categoria/editar_categoria.html'
    success_url = reverse_lazy('listado_categorias')

class Eliminar_Categoria(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url='/administrador/ingreso/'
    redirect_field_name = 'redirect_to'
    permission_required = 'usuarios.es_administrador'

    model = Categoria
    form_class = CategoriaForm
    template_name = 'admin/categoria/eliminar_categoria.html'
    success_url = reverse_lazy('listado_categorias')



@login_required(login_url='/administrador/ingreso/')
@permission_required('usuarios.es_administrador', raise_exception=True)
def Registro_Repartidor(request):
    repartidor = RepartidorForm()
    tel = TelefonoForm()
    if request.method == 'POST' :
        repartidor = RepartidorForm(request.POST)
        tel = TelefonoForm(request.POST)
        if repartidor.is_valid() and tel.is_valid():
            subject = 'Bienvenido a la Trajinera Digital!'
            message = 'El equipo Quetzal te da la Bienvenida tu contraseña es ' + str(repartidor.cleaned_data['password1']) + ' Accede con tu correo electronico'
            recepient = str(repartidor.cleaned_data['email'])
            send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            user = repartidor.save()
            permiso = Permission.objects.get(name='Acceso_Repartidor')
            user.user_permissions.add(permiso)
            rep = tel.save(commit=False)
            rep.user = user
            rep.save()
            return redirect('index_menu')
    return render(
        request, 
        'admin/repartidor/registro_repartidor.html', 
        {'form': repartidor, 'tel' : tel}
    )

"""def Registro_Repartidor(request):
    repartidor = RepartidorForm()
    if request.method == 'POST' :
        repartidor = RepartidorForm(request.POST)
        if repartidor.is_valid() :
            subject = 'Bienvenido a la Trajinera Digital!'
            message = 'El equipo Quetzal te da la Bienvenida tu contraseña es ' + str(repartidor.cleaned_data['contrasena']) + ' Accede con tu correo electronico'
            recepient = str(repartidor.cleaned_data['correo'])
            send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            repartidor.save()
            return redirect('index_menu')
    return render(request, 'admin/repartidor/registro_repartidor.html', {'form': repartidor})
"""


class ordenes_entregadas(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url='/administrador/ingreso/'
    redirect_field_name = 'redirect_to'
    permission_required = 'usuarios.es_administrador'

    model = Orden
    template_name = 'admin/ordenes/ordenes_entregadas.html'


class ordenes_pendientes(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url='/administrador/ingreso/'
    redirect_field_name = 'redirect_to'
    permission_required = 'usuarios.es_administrador'

    model = Orden
    template_name = 'admin/ordenes/ordenes_pendientes.html'

@login_required(login_url='/administrador/ingreso/')
@permission_required('usuarios.es_administrador', raise_exception=True)
def orden_alimentos(request,pk):
    orden = Orden.objects.get(id = pk)
    alimentos = orden.alimentos_orden.all()
    contexto = {'orden': alimentos}
    return render(request, 'admin/ordenes/detalle_orden.html', contexto)


class Cambiar_estado(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url='/administrador/ingreso/'
    redirect_field_name = 'redirect_to'
    permission_required = 'usuarios.es_administrador'

    model = Orden
    form_class = OrdenesForm
    template_name = 'admin/ordenes/cambiar_estado.html'
    success_url = reverse_lazy('ordenes_pendientes')

def ingreso_repartidor(request):
    if request.user.is_authenticated:
        return redirect('/administrador/index_repartidor')

    if request.method == 'POST':
        form = IngresoForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)

            return redirect('/administrador/index_repartidor/')
        else:

            return render(
                request,
                'autenticacion/login_repartidor.html',
                {'form' : form}
            )
    else:
        form = IngresoForm()
        args = {'form' : form}

        return render(request, "autenticacion/login_repartidor.html", args) 


@login_required(login_url='/administrador/ingreso_repartidor/')
@permission_required('usuarios.es_repartidor', raise_exception=True)
def indexRepartidor(request):
    return render(request,'repartidor/index_repartidor.html')


@login_required(login_url='/administrador/ingreso_repartidor/')
@permission_required('usuarios.es_repartidor', raise_exception=True)
def salir_repartidor(request):
    logout(request)

    return redirect('/administrador/ingreso_repartidor/') 

class ordenes_entregadas_repartidor(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url='/administrador/ingreso_repartidor/'
    redirect_field_name = 'redirect_to'
    permission_required = 'usuarios.es_repartidor'

    model = Orden
    template_name = 'repartidor/ordenes/ordenes_entregadas_repartidor.html'


class ordenes_pendientes_repartidor(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url='/administrador/ingreso_repartidor/'
    redirect_field_name = 'redirect_to'
    permission_required = 'usuarios.es_repartidor'

    model = Orden
    template_name = 'repartidor/ordenes/ordenes_pendientes_repartidor.html'

class ordenes_disponibles_repartidor(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url='/administrador/ingreso_repartidor/'
    redirect_field_name = 'redirect_to'
    permission_required = 'usuarios.es_repartidor'

    model = Orden
    template_name = 'repartidor/ordenes/ordenes_disponibles.html'

def aceptar_orden(request,pk):
    orden = Orden.objects.get(id = pk)
    contexto = {'pedido': orden}
    return render(request,'repartidor/ordenes/orden.html', contexto)

def confirmar_orden_repartidor(request, pk1, pk2):
    orden = Orden.objects.get(id = pk1)
    usuario = User.objects.get(id = pk2)
    repartidor = Repartidor.objects.get(user = usuario)
    orden.repartidor_orden = repartidor
    orden.save()
    contexto = {'Pedido': orden, 'Repartidor': repartidor}
    return render(request,'repartidor/ordenes/orden_repartidor.html',contexto)


def orden_entregada(request, pk):
    orden = Orden.objects.get(id = pk)
    contexto = {'pedido': orden}
    return render(request,'repartidor/ordenes/orden_entregada.html',contexto)

def confirmar_entrega(request,pk):
    orden = Orden.objects.get(id = pk)
    estado = Estado.objects.get(id = 4)
    orden.estado_orden = estado
    orden.save()
    contexto = {'Pedido': orden}
    return render(request,'repartidor/ordenes/confirmar_entrega.html', contexto)
