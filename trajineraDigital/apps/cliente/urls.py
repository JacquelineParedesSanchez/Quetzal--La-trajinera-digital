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

urlpatterns = [
    path('', views.login, name='login'),
    path('login/', v.LoginView.as_view(), {'template_name': 'login.html'}, name='login'),
    path('registro/', views.registro, name='registro'),
    path('principal/', views.principal, name='principal'),
    path('menu/', views.menu, name='menu'),
    path('carrito/', views.carrito, name='carrito'),
]