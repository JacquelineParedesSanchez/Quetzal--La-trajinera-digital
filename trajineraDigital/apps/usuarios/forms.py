from django import forms
from apps.menu.models import * 
from apps.usuarios.models import * 
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

"""class RepartidorForm(forms.ModelForm):

	class Meta:

		model = Repartidor

		fields = [
			'nombre',
			'apellidos',
			'correo',
			'contrasena', 
		]

		labels = {
			'nombre': 'Nombre',
			'apellidos': 'Apellidos',
			'correo': 'Email',
			'contrasena': 'Password',
		}

		widgets = {
			'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
			'apellidos': forms.TextInput(attrs = {'class': 'form-control'}),
			'correo': forms.TextInput(attrs = {'class': 'form-control'}),
			'contrasena': forms.TextInput(attrs = {'class': 'form-control'}),
		}"""

class RepartidorForm(UserCreationForm):
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2'
		]

	def clean_email(self):
		data = self.cleaned_data['email']

		if User.objects.filter(email=data).count() > 0:
			raise forms.ValidationError("Este email ya está registrado.")

		return data

	def save(self, commit=True):
		user = super(RepartidorForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user

class TelefonoForm(forms.ModelForm):
	tel = RegexValidator(r'^(55)\d{8}', "El número debe estár en formato LADA.")
	telefono = forms.CharField(validators=[tel], max_length=10)

	class Meta:
		model = Repartidor
		fields = ['telefono']

	def clean_telefono(self):
		data = self.cleaned_data['telefono']

		if Repartidor.objects.filter(telefono=data).count() > 0:
			raise forms.ValidationError("Este telefono ya está registrado.")

		return data



class AlimentoForm(forms.ModelForm):
	class Meta:
		model = Alimento 
		fields = [
			'nombre',
			'precio',
			'descripcion',
			'categoria',
			'foto',
		]
		labels = {
			'nombre': 'Nombre' ,
			'precio': 'Precio' ,
			'descripcion': 'Descripcion' ,
			'categoria': 'Categoria' ,
			'foto': 'Foto' ,
		}
		widgets = {
			'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
			'precio': forms.NumberInput(),
			'descripcion': forms.TextInput(attrs = {'class': 'form-control'}),
			
		}



class CategoriaForm(forms.ModelForm):
	class Meta:
		model = Categoria
		fields = [
			'nombre',
			'descripcion',
			'foto',
		]
		labels = {
			'nombre': 'Nombre',
			'descripcion': 'Descripcion',
			'foto': 'Foto',
		}
		widgets = {
			'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
			'descripcion': forms.TextInput(attrs = {'class': 'form-control'}),
		}


class OrdenesForm(forms.ModelForm):
	class Meta:
		model = Orden
		fields = [
			'estado_orden',
		]
		labels = {
			'estado_orden': 'Estado de la Orden',
		}

class IngresoForm(AuthenticationForm):
	def clean(self):
		username = self.data["username"]
		password = self.data["password"]

		if User.objects.filter(username=username).count() == 0:
			#raise forms.ValidationError(
			#	"El usuario o la contraseña son incorrectos"
			#)
			self.add_error(
				"username", 
				forms.ValidationError(
					"El usuario o la contaseña son incorrectos."
				)
			)

		user = authenticate(username=username, password=password)
		if user is None:
			#raise forms.ValidationError(
			#	"El usuario o la contraseña son incorrectos"
			#)
			self.add_error(
				"password", 
				forms.ValidationError(
					"El usuario o la contraseña son incorrectos."
				)
			)
		"""else:
			adm = Administrador.objects.filter(user=user).first()
			if adm is None:
				raise forms.ValidationError(
					"Acceso denegado"
				)"""
				#self.add_error(
		      	#	"username", 
		      	#	forms.ValidationError(
		     	#		"Acceso denegado."
		      	#	)
				#)
