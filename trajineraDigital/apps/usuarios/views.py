from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from apps.menu.models import Alimento, Categoria, Orden
from apps.usuarios.forms import AlimentoForm, CategoriaForm, RepartidorForm, OrdenesForm
from trajineraDigital.settings import EMAIL_HOST_USER
from django.core.mail import send_mail 


# Create your views here.

def indexAdministrador(request):
	return render(request,'admin/index_admin.html')



class menu_Alimentos_Administrador(ListView):
	model = Alimento
	template_name = 'admin/alimento/alimento.html'

class menu_Alimentos_Editar(ListView):
	model = Alimento
	template_name = 'admin/alimento/menu_editar_alimento.html'

class menu_Alimentos_Eliminar(ListView):
	model = Alimento
	template_name = 'admin/alimento/menu_eliminar_alimento.html'


class Crear_Alimento(CreateView):
	model = Alimento
	form_class = AlimentoForm
	template_name = 'admin/alimento/crear_alimento.html'
	success_url = reverse_lazy('menu_alimentos')

class Editar_Alimento(UpdateView):
	model = Alimento
	form_class = AlimentoForm
	template_name = 'admin/alimento/editar_alimento.html'
	success_url = reverse_lazy('menu_alimentos')

class Eliminar_Alimento(DeleteView):
	model = Alimento
	form_class = AlimentoForm
	template_name = 'admin/alimento/eliminar_alimento.html'
	success_url = reverse_lazy('menu_alimentos')




class menu_Categoria(ListView):
	model = Categoria
	template_name = 'admin/categoria/categorias.html'


def menu_Categoria_Alimentos(request, categoria):
	alimento = Alimento.objects.all()
	contexto = {'alimentos': alimento, 'Categoria': categoria }
	return render(request, 'admin/categoria/alimentos_categoria.html', contexto) 


class menu_Editar_Categoria(ListView):
	model = Categoria
	template_name = 'admin/categoria/menu_editar_categoria.html'

class menu_Eliminar_Categoria(ListView):
	model = Categoria
	template_name = 'admin/categoria/menu_eliminar_categoria.html'


class Crear_Categoria(CreateView):
	model = Categoria
	form_class = CategoriaForm
	template_name = 'admin/categoria/crear_categoria.html'
	success_url = reverse_lazy('listado_categorias')

class Editar_Categoria(UpdateView):
	model = Categoria
	form_class = CategoriaForm
	template_name = 'admin/categoria/editar_categoria.html'
	success_url = reverse_lazy('listado_categorias')

class Eliminar_Categoria(DeleteView):
	model = Categoria
	form_class = CategoriaForm
	template_name = 'admin/categoria/eliminar_categoria.html'
	success_url = reverse_lazy('listado_categorias')




def Registro_Repartidor(request):
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



class ordenes_entregadas(ListView):
	model = Orden
	template_name = 'admin/ordenes/ordenes_entregadas.html'


class ordenes_pendientes(ListView):
	model = Orden
	template_name = 'admin/ordenes/ordenes_pendientes.html'


def orden_alimentos(request,pk):
	orden = Orden.objects.get(id = pk)
	alimentos = orden.alimentos_orden.all()
	contexto = {'orden': alimentos}
	return render(request, 'admin/ordenes/detalle_orden.html', contexto)


class Cambiar_estado(UpdateView):
	model = Orden
	form_class = OrdenesForm
	template_name = 'admin/ordenes/cambiar_estado.html'
	success_url = reverse_lazy('ordenes_pendientes')


