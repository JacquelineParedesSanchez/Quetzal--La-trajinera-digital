from django.urls import path
from apps.usuarios.views import *

urlpatterns = [

    #URLS Administrador
    path('index_administrador/', indexAdministrador, name = 'index_menu'),
    
    path('ingreso/', ingreso, name='ingreso'),
    path('salir/', salir, name='salir'),

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


    #ULRS Repartidor
    path('index_repartidor/', indexRepartidor, name = 'index_menu_repartidor'),

    path('ingreso_repartidor/', ingreso_repartidor, name='ingreso_repartidor'),
    path('salir_repartidor/', salir_repartidor, name='salir_repartidor'),

    path('ordenes_entregadas_repartidor/', ordenes_entregadas_repartidor.as_view(),name = 'ordenes_entregadas_repartidor'),
    path('ordenes_pendientes_repartidor/', ordenes_pendientes_repartidor.as_view(),name = 'ordenes_pendientes_repartidor'),
    path('ordenes_disponibles_repartidor/', ordenes_disponibles_repartidor.as_view(),name = 'ordenes_disponibles_repartidor'),
    path('aceptar_orden/<pk>', aceptar_orden , name = 'aceptar_orden'),
    path('orden_repartidor/<pk1>/<pk2>', confirmar_orden_repartidor , name = 'confirmar_orden'),
    path('orden_entregada/<pk>', orden_entregada , name = 'orden_entregada'),
    path('confirmar_entrega/<pk>', confirmar_entrega , name = 'confirmar_entrega'),
]