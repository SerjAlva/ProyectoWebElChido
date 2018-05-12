from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(primary_key=True)
    nombre = models.CharField(50)
    marca = models.CharField(50)
    proveedor = models.CharField(50)
    precio = models.IntegerField
    cantidad = models.IntegerField
