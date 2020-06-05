from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import UserCliente

class SignUpForm(UserCreationForm):
	email = forms.EmailField(required=True)
	#direccion = forms.CharField(max_length=500)
	#tel = RegexValidator(r'^(55)\d{8}', "El número debe estár en formato LADA.")
	#telefono = forms.CharField(validators=[tel], max_length=10)

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			#'direccion',
			#'telefono',
			'password1',
			'password2']

	def clean_email(self):
		data = self.cleaned_data['email']

		if User.objects.filter(email=data).count() > 0:
			raise forms.ValidationError("Este email ya está registrado.")

		return data

	def save(self, commit=True):
		user = super(SignUpForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
		#user.telefono = self.cleaned_data['telefono']
		#user.direccion = self.cleaned_data['direccion']

		if commit:
			user.save()

		return user

class RegistroClienteForm(forms.ModelForm):
	direccion = forms.CharField(max_length=500)
	tel = RegexValidator(r'^(55)\d{8}', "El número debe estár en formato LADA.")
	telefono = forms.CharField(validators=[tel], max_length=10)

	class Meta:
		model = UserCliente
		fields = ['direccion', 'telefono']

"""class LoginForm(AutenticationFrom):

	def clean(self):
		email = self.data["email"]
		password = self.data["password"]

		if User.objects.filter(email=email).count() == 0:
			self.add_error(
				"email", forms.ValidationError("No hay cuenta vinculada a este número.")
				)

		user = authenticate(username=username, password=password)
		if user is None:
			self.add_error("password", forms.ValidationError("Wrong password."))
"""
