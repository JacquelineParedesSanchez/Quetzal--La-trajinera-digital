from django.urls import path
from apps.usuarios.views import *

urlpatterns = [
    path('index_administrador/', indexAdministrador, name = 'index_menu'),
    
    path('menu_Alimentos_Administrador/', menu_Alimentos_Administrador.as_view() , name = 'menu_alimentos'),
    path('menu_Alimentos_Editar/', menu_Alimentos_Editar.as_view() , name = 'menu_editar_alimentos'),
    path('menu_Alimentos_Eliminar/', menu_Alimentos_Eliminar.as_view() , name = 'menu_eliminar_alimentos'),
    path('menu_Alimentos_crear/', Crear_Alimento.as_view() , name = 'crear_alimento'),
    path('editar_Alimento/<pk>', Editar_Alimento.as_view() , name = 'editar_alimento'),
    path('eliminar_Alimento/<pk>', Eliminar_Alimento.as_view() , name = 'eliminar_alimento'),
    
    path('menu_Categorias/', menu_Categoria.as_view() , name = 'listado_categorias'),
    path('menu_Categorias_Editar/', menu_Editar_Categoria.as_view() , name = 'listado_editar_categorias'),
    path('menu_Categorias_Eliminar/', menu_Eliminar_Categoria.as_view() , name = 'listado_eliminar_categorias'),
    path('menu_Categorias_crear/', Crear_Categoria.as_view() , name = 'crear_categoria'),
    path('editar_Categoria/<pk>', Editar_Categoria.as_view() , name = 'editar_categoria'),
    path('eliminar_Categoria/<pk>', Eliminar_Categoria.as_view() , name = 'eliminar_categoria'),
    path('Categoria_Alimentos/<categoria>', menu_Categoria_Alimentos , name = 'categoria_alimentos'),

    path('registro_repartidor/', Registro_Repartidor ,name = 'repartidor_registro'),  

    path('ordenes_entregadas/', ordenes_entregadas.as_view(),name = 'ordenes_entregadas'),
    path('ordenes_pendientes/', ordenes_pendientes.as_view(),name = 'ordenes_pendientes'),
    path('orden_alimentos/<pk>', orden_alimentos ,name = 'orden_alimentos'),
    path('cambiar_estado/<pk>', Cambiar_estado.as_view() , name = 'cambiar_estado'),

]