
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from apps.cliente.forms import SignUpForm

#from users.

# Create your views here.
#class SignUpView(View):

def login(request):
    numbers = [1,2,3,4,5]
    name= "Max Power"

    args={'myname' : name, 'numbers': numbers}
    return render(request, "cliente/home.html", args)

def registro(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')
        else:
            print(form.errors)
    else:
        form=SignUpForm()

        args = {'form': form}
        return render(request, 'registration/register.html', args)
