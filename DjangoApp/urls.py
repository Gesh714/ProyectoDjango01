from django.urls import path
from DjangoApp import  views

urlpatterns = [
    path('', views.home, name='inicio'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('cargar_curso_plantilla/',  views.cargarCursosPlantilla, name='cargar_cursos_plantilla'),
    path('cargar_curso_manual/', views.cargarCursosManual,  name='cargar_curso_manual'),
    path('cargar_participante_plantilla/', views.cargarParticipantePlantilla, name='cargar_participante_plantilla'),
    path('cargar_participante_manual/', views.cargarParticipanteManual, name='cargar_participante_manual'),
    path('ver_cursos/', views.verCursos, name='ver_cursos'),
    path('ver_participantes/', views.verParticipantes, name='ver_participantes'),

]