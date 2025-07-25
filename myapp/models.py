from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.apellido}, {self.nombre} y soy profesor de {self.profesion}"

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad_alumnos = models.IntegerField()
    fecha_inicio = models.DateField()

    def __str__(self):
        return f"Este curso de {self.nombre}, se inicia el {self.fecha_inicio}"