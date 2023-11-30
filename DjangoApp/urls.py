from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from DjangoApp import views

urlpatterns = [
    path('', views.home, name='inicio'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('cargar_curso_plantilla/',  views.cargarCursosPlantilla, name='cargar_cursos_plantilla'),
    path('cargar_participante_plantilla/', views.cargarParticipantePlantilla, name='cargar_participante_plantilla'),
    path('ver_cursos/', views.verCursos, name='ver_cursos'),
    path('ver_participantes/', views.verParticipantes, name='ver_participantes'),
    path('curso/<int:pk>', views.curso_info, name='curso'),
    path('participante/<int:pk>', views.participante_info, name='participante'),
    path('delete_curso/<int:pk>', views.delete_curso, name='delete_curso'),
    path('delete_participante/<int:pk>', views.delete_participante, name='delete_participante'),
    path('add_curso/', views.add_curso, name='add_curso'),
    path('add_participante/', views.add_participante, name='add_participante'),
    path('update_curso/<int:pk>', views.update_curso, name='update_curso'),
    path('update_participante/<int:pk>', views.update_participante, name='update_participante'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)