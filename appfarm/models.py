from statistics import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model): 
    nombre = models.CharField(max_length=50)

    def __str__(self):
        fila = self.nombre 
        return fila

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.CharField(max_length=50, verbose_name='Descripción')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    precio = models.IntegerField(verbose_name='Precio')
    imagen = models.ImageField(upload_to='imagenes/', null=True, verbose_name='Producto')
    
    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + "Descripción: " + self.descripcion
        return fila

    def delete(self, using=None, keep_parents= False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()   



      
   
    