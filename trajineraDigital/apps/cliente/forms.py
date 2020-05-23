from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#from music.models import Cliente

class SignUpForm(forms.ModelForm):
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			#'direccion',
			#'telefono',
			'email',
			'password',
			]

	def save(self, commit=True):
		user = super(SignUpForm, self).save(commit=False)

		user.first_name = self.cleaned_data['first_name']

		user.last_name = self.cleaned_data['last_name']

		user.telefono = self.cleaned_data["telefono"]
		if User.objects.filter(name=telefono).count() > 0:
			raise forms.ValidationError("El número ya está vinculado a otra cuenta.")

		user.email = self.cleaned_data['email']
		if User.objects.filter(name=email).count > 0:
			raise forms.ValidationError("Este email ya esta registrado.")

		if commit:
			user.save()

		return user

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
