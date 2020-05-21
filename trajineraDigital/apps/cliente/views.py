
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form=UserCreationForm()

        args = {'form': form}
        return render(request, 'registration/register.html', args)
