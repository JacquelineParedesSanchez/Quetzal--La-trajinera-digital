"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth import views as v

app_name="cliente"
urlpatterns = [
    path('', views.menu, name='home'),
    path('login/', views.ingreso, name='ingreso'),
    #path('login/', v.LoginView.as_view(), {'template_name': 'login.html'}, name='login'),
    #path('logout/', v.LogoutView.as_view(),name = 'logged_out'),
    path('logout/', views.salir, name='salir'),
    path('registro/', views.registro, name='registro'),
    path('principal/', views.principal, name='principal'),
    path('menu/', views.menu, name='menu'),
    path('carrito/', views.carrito, name='carrito'),
    path('carta/<pk>', views.ver_menu, name='ver_menu'),
    path('carrito/<pk>', views.agrega_carrito, name='agrega_carrito'),
    path('orden/', views.registra_orden, name='registra_orden'),
    path('ordenes/', views.ver_ordenes, name='ver_ordenes'),
    path('orden_alimentos/<pk>', views.orden_alimentos, name='orden_alimentos'),
    path('cuenta/', views.cuenta, name='cuenta'),
    path('cambiar_info/', views.cambiar_info, name='cambiar_info')
]
