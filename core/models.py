from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=10, unique=True)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre




class Producto(models.Model):
    codigo = models.CharField(max_length=5, unique=True)
    modelo = models.CharField(max_length=50)
    precio = models.IntegerField()
    color = models.CharField(max_length=30)
    talla = models.CharField(max_length=30)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE) 
    imagen = models.ImageField(upload_to="productos", null= True)

    class Meta:
        verbose_name_plural = "Productos"


    def __str__(self):
        return self.codigo