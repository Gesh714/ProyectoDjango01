from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from cargar_planillas import views

urlpatterns = [
    path('upload_participantes/', views.upload_participante, name='upload_participante'),
    path('upload_cursos/', views.upload_curso, name='upload_curso'),
    path('upload_relator/', views.upload_relator, name='upload_relator'),
]