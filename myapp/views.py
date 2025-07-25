from django.shortcuts import render
from .models import Estudiante, Profesor, Curso
from .forms import EstudianteForm, ProfesorForm, CursoForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

# ESTUDIANTES ---------------------------------------------------------------
def estudiante_list(request):
    search = request.GET.get('search', None)
    if search:
        estudiantes = Estudiante.objects.filter(nombre__icontains=search)
    else:
        estudiantes = Estudiante.objects.all()
    return render(request, 'myapp/estudiantes/estudiante_list.html', {'estudiantes': estudiantes})

def estudiante_detail(request, estudiante_id):
    estudiante = Estudiante.objects.get(id=estudiante_id)
    return render(request, 'myapp/estudiantes/estudiante_detail.html', {'estudiante': estudiante})

def estudiante_create(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            estudiante = Estudiante.objects.create(
                nombre=request.POST['nombre'],
                apellido=request.POST['apellido'],
                edad=request.POST['edad'],
                email=request.POST['email']
            )
            estudiante.save()
            return redirect('estudiante_list')
    else:
        form = EstudianteForm()
    return render(request, 'myapp/estudiantes/estudiante_create.html', {'form': form})

# PROFESORES ----------------------------------------------------------------

def profesor_list(request):
    search = request.GET.get('search', None)
    if search:
        profesores = Profesor.objects.filter(nombre__icontains=search)
    else:
        profesores = Profesor.objects.all()
    return render(request, 'myapp/profesores/profesor_list.html', {'profesores': profesores})

def profesor_detail(request, profesor_id):
    profesor = Profesor.objects.get(id=profesor_id)
    return render(request, 'myapp/profesores/profesor_detail.html', {'profesor': profesor})

def profesor_create(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            profesor = Profesor.objects.create(
                nombre=request.POST['nombre'],
                apellido=request.POST['apellido'],
                profesion=request.POST['profesion'],
                email=request.POST['email']
            )
            profesor.save()
            return redirect('profesor_list')
    else:
        form = ProfesorForm()
    return render(request, 'myapp/profesores/profesor_create.html', {'form': form})

# CURSOS --------------------------------------------------------------------

def curso_list(request):
    search = request.GET.get('search', None)
    if search:
        cursos = Curso.objects.filter(nombre__icontains=search)
    else:
        cursos = Curso.objects.all()
    return render(request, 'myapp/cursos/curso_list.html', {'cursos': cursos})

def curso_detail(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    return render(request, 'myapp/cursos/curso_detail.html', {'curso': curso})

def curso_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = Curso.objects.create(
                nombre=request.POST['nombre'],
                comision=request.POST['comision'],
                profesor=request.POST['profesor']
            )
            curso.save()
            return redirect('curso_list')
    else:
        form = CursoForm()
    return render(request, 'myapp/cursos/curso_create.html', {'form': form})