from django.db import models

# Create your models here.


class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)