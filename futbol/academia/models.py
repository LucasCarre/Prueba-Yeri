from django.db import models

# Create your models here.
class Categorias(models.Model):
    año = models.IntegerField(max_length=40)
    nivel=models.CharField(max_length=50)

class Alumnos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(max_length=40)

class Profesores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nivel= models.CharField(max_length=50)
    telefono= models.IntegerField(max_length=40)
