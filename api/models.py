from django.db import models

# Create your models here.


class Mascota(models.Model):
    GENERO_CHOICES = [
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
    ]
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES)
    fecha_nacimiento = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    
class RegistrosBase(models.Model):
    GENERO_CHOICES = [
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
    ]
    raza = models.CharField(max_length=50)
    peso_minimo = models.DecimalField(max_digits=5, decimal_places=2)
    peso_maximo = models.DecimalField(max_digits=5, decimal_places=2)
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES)