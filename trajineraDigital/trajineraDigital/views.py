from django.shortcuts import redirect, render
from django.http import HttpResponse

def login_redirect(request):
    return redirect('/home/login')

def bienvenida(request):
	return render(request,'index.html')
