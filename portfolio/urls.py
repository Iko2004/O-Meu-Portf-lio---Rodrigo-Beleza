from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('percurso/', views.percurso_view, name='percurso'),
    path('makingofs/', views.makingofs_view, name='makingofs'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('contactos/', views.contactos_view, name='contactos'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('tecnologias/eliminar/<int:id>/', views.eliminar_tecnologia, name='eliminar_tecnologia'),
    path('tecnologias/editar/<int:id>/', views.editar_tecnologia, name='editar_tecnologia'),
    path('projetos/eliminar/<int:id>/', views.eliminar_projeto, name='eliminar_projeto'),
    path('projetos/editar/<int:id>/', views.editar_projeto, name='editar_projeto'),
    path('percurso/editar/<int:id>/', views.editar_licenciatura, name='editar_licenciatura'),
    path('percurso/eliminar/<int:id>/', views.eliminar_licenciatura, name='eliminar_licenciatura'),
    path('percurso/eliminar-formacao/<int:id>/', views.eliminar_formacao, name='eliminar_formacao'),
]