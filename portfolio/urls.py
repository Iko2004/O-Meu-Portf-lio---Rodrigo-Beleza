from django.urls import path
from . import views

urlpatterns = [
    # Páginas Principais
    path('', views.home_view, name='home'),
    path('contactos/', views.contactos_view, name='contactos'),
    path('makingofs/', views.makingofs_view, name='makingofs'),

    # Projetos
    path('projetos/', views.projetos_view, name='projetos'),
    path('projetos/editar/<int:id>/', views.editar_projeto, name='editar_projeto'),
    path('projetos/eliminar/<int:id>/', views.eliminar_projeto, name='eliminar_projeto'),

    # Tecnologias
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tecnologias/editar/<int:id>/', views.editar_tecnologia, name='editar_tecnologia'),
    path('tecnologias/eliminar/<int:id>/', views.eliminar_tecnologia, name='eliminar_tecnologia'),

    # Percurso Académico / Formações
    path('percurso/', views.percurso_view, name='percurso'),
    # AQUI ESTÁ A CORREÇÃO PRINCIPAL:
    path('percurso/editar/<int:id>/', views.editar_formacao, name='editar_formacao'),
    path('percurso/eliminar/<int:id>/', views.eliminar_formacao, name='eliminar_formacao'),

    # Competências
    path('competencias/', views.competencias_view, name='competencias'),
    path('competencias/editar/<int:id>/', views.editar_competencia, name='editar_competencia'),
    path('competencias/eliminar/<int:id>/', views.eliminar_competencia, name='eliminar_competencia'),

    #Sobre aplicação
    path('sobre/', views.sobre_view, name='sobre'),
]
