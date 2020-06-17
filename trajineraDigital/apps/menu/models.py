from django.db import models
from apps.usuarios.models import Repartidor
from apps.cliente.models import UserCliente

# Create your models here.
class Estado(models.Model):
	
	nombre = models.CharField(max_length=15)
	
	def __str__(self):
		return '{} {}'.format(self.id,self.nombre)

class Categoria(models.Model):
	
	nombre = models.CharField(max_length = 30)
	descripcion = models.TextField(null=True)
	foto = models.ImageField(null = True ,upload_to='categorias/images/')
	

	def __str__(self):
		return '{}'.format(self.nombre)

class Alimento(models.Model):

	nombre = models.CharField(max_length = 30)
	precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
	descripcion = models.TextField()
	categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
	foto = models.ImageField(upload_to='alimentos/images/')
	
	def __str__(self):
		return '{}'.format(self.nombre)



class Orden(models.Model):

	fecha_orden = models.DateTimeField()
	estado_orden = models.ForeignKey(Estado, null=True , blank=True, on_delete=models.CASCADE)
	orden = models.ForeignKey(UserCliente, null=True , blank=True, on_delete=models.CASCADE)
	repartidor_orden = models.ForeignKey(Repartidor, null=True , blank=True, on_delete=models.CASCADE)
	alimentos_orden = models.ManyToManyField(Alimento, blank=True)
	precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

	def __str__(self):
		return 'Orden numero: {}'.format(self.id)
