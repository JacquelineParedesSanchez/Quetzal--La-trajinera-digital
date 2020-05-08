from django import forms
from django.contrib.auth.forms import AutenticationFrom
from django.contrib.auth import authenticate

from music.models import Cliente

class SignUpForm(forms.ModelForm):

	class Meta:
		model = Cliente
		fields = ['first_name', 'last_name', 'email', 
			'password', 'direccion', 'telefono']

	def clean_email(self):
		email = self.cleaned_data["email"]

		if Cliente.objects.filter(name=email).count > 0:
			raise forms.ValidationError("El email ya existe.")

	def clean_telefono(self): 
		telefono = self.cleaned_data["telefono"]

		if Cliente.objects.filter(name=telefono).count() > 0:
			raise forms.ValidationError("El número ya está vinculado a otra cuenta.")

class LoginForm(AutenticationFrom):

	def clean(self):
		email = self.data["email"]
		password = self.data["password"]

		if Cliente.objects.filter(email=email).count() == 0:
			self.add_error(
				"email", forms.ValidationError("No hay cuenta vinculada a este número.")
				)

		cliente = authenticate(username=username, password=password)
		if cliente is None:
			self.add_error("password", forms.ValidationError("Wrong password."))