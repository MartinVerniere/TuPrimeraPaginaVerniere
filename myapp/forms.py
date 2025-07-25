from django import forms
from .models import Estudiante, Profesor, Curso
from django.forms.widgets import DateInput

class EstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre del Estudiante')
    apellido = forms.CharField(max_length=100, label='Apellido del Estudiante')
    email = forms.EmailField(label='Email del Estudiante')
    edad = forms.IntegerField(label='Edad del Estudiante')

    def save(self, commit=True):
        # Crear una instancia del modelo Estudiante con los datos del formulario
        estudiante = Estudiante(
            nombre=self.cleaned_data['nombre'],
            apellido=self.cleaned_data['apellido'],
            email=self.cleaned_data['email'],
            edad=self.cleaned_data['edad']
        )
        if commit:
            estudiante.save()
        return estudiante

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre del Profesor')
    apellido = forms.CharField(max_length=100, label='Apellido del Profesor')
    email = forms.EmailField(label='Email del Profesor')
    profesion = forms.CharField(max_length=100, label='Profesion del Profesor')

    def save(self, commit=True):
        # Crear una instancia del modelo Profesor con los datos del formulario
        profesor = Profesor(
            nombre=self.cleaned_data['nombre'],
            apellido=self.cleaned_data['apellido'],
            email=self.cleaned_data['email'],
            profesion=self.cleaned_data['profesion']
        )
        if commit:
            profesor.save()
        return profesor
    
class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre del curso')
    capacidad_alumnos = forms.IntegerField(label='Capacidad de alumnos del curso')
    fecha_inicio = forms.DateField(label='Fecha de inicio del curso', widget=DateInput(attrs={'type': 'date'}))

    def save(self, commit=True):
        # Crear una instancia del modelo Curso con los datos del formulario
        curso = Curso(
            nombre=self.cleaned_data['nombre'],
            capacidad_alumnos=self.cleaned_data['capacidad_alumnos'],
            fecha_inicio=self.cleaned_data['fecha_inicio']
        )
        if commit:
            curso.save()
        return curso