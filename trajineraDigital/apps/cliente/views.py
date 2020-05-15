
from django.shortcuts import render, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

#from users.

# Create your views here.
#class SignUpView(View):

def login(request):
    return render(request, "cliente/login.html")
#    return render()
#    return HttpResponse("Prueba hecha")
