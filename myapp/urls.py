from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('estudiantes/', views.estudiante_list, name='estudiante_list'),
    path('profesores/', views.profesor_list, name='profesor_list'),
    path('cursos/', views.curso_list, name='curso_list'),
]
