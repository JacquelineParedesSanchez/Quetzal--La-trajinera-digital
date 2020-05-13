from django.http import HttpResponse
from django.shortcuts import render

#from users.

# Create your views here.
#class SignUpView(View):

def home_view(*args, **kwargs):
    return HttpResponse("<h1> Bienvenido </h1>")
