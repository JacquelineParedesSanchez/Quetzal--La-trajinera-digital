from django.db import models

# Create your models here.
class Estado(models.Model):

	nombre = models.CharField(max_length=15)

	def __str__(self):
		return '{}'.format(self.nombre)



class Alimento(models.Model):

	nombre = models.CharField(max_length=30)
	precio = models.IntegerField()
	descripcion = models.TextField()
	foto = models.ImageField(upload_to='media/alimentos/images/')

	def __str__(self):
		return '{}'.format(self.nombre)



class Categoria(models.Model):

	nombre = model.CharField(max_length = 30)
	lista_alimentos = models.ManyToManyField(Alimento, blank=True)

	def __str__(self):
		return '{}'.format(self.nombre)


class Orden(models.Model):

	fecha_orden = models.DateField()
	estado_orden = models.ForeignKey(Estado, null=True , blank=True, on_delete=models.CASCADE)
	alimentos_orden = models.ManyToManyField(Alimento, blank=True)

	def __str__(self):
		return 'Orden numero: {}'.format(self.id)