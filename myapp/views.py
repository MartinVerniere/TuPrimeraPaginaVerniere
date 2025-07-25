from django.shortcuts import render
from .models import Estudiante, Profesor, Curso

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def estudiante_list(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'myapp/estudiante_list.html', {'estudiantes': estudiantes})

def profesor_list(request):
    profesores = Profesor.objects.all()
    return render(request, 'myapp/profesor_list.html', {'profesores': profesores})

def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'myapp/curso_list.html', {'cursos': cursos})