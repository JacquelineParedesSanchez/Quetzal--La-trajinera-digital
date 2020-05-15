
from django.shortcuts import render, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

#from users.

# Create your views here.
#class SignUpView(View):

def registro(response):
#    form = UserCreation()
#    return render(response, "registro/registro.html", {"form":form})
#    return render()
    return HttpResponse("Prueba hecha")
