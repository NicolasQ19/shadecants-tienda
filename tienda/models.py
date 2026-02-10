from django.db import models

# Create your models here.
from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Perfume(models.Model):
    GENEROS = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('U', 'Unisex'),
    )
    
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    genero = models.CharField(max_length=1, choices=GENEROS)
    imagen = models.ImageField(upload_to='perfumes/', blank=True, null=True)
    destacado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.marca} - {self.nombre}"

class Variante(models.Model):
    perfume = models.ForeignKey(Perfume, related_name='variantes', on_delete=models.CASCADE)
    mililitros = models.IntegerField(choices=[(2, '2ml'), (5, '5ml'), (10, '10ml'), (30, '30ml')])
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=10)

    def __str__(self):
        return f"{self.perfume.nombre} - {self.mililitros}ml (${self.precio})"