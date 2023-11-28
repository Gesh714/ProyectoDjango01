from django.contrib import admin

# Register your models here.
from .models import Cursos, Inscritos

admin.site.register(Cursos)

admin.site.register(Inscritos)
