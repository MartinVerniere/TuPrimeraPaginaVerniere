from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('estudiantes/', views.estudiante_list, name='estudiante_list'),
    path('profesores/', views.profesor_list, name='profesor_list'),
    path('cursos/', views.curso_list, name='curso_list'),

    path('estudiantes/<int:estudiante_id>/', views.estudiante_detail, name='estudiante_detail'),
    path('profesores/<int:profesor_id>/', views.profesor_detail, name='profesor_detail'),
    path('cursos/<int:curso_id>/', views.curso_detail, name='curso_detail'),

    path('estudiantes/create/', views.estudiante_create, name='estudiante_create'),
    path('profesores/create/', views.profesor_create, name='profesor_create'),
    path('cursos/create/', views.curso_create, name='curso_create'),
]
