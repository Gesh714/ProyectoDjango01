from django.db import models

# Create your models here.
class Cursos(models.Model):
    nombre_curso = models.CharField(max_length=500)
    id_sence = models.IntegerField()
    comuna = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    modalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_curso

class Inscritos(models.Model):
    nombre_completo = models.CharField(max_length=200, editable=True)
    rut = models.CharField(max_length=10, editable=True)
    fecha_nac = models.DateField()
    genero = models.CharField(max_length=100)
    img_ci_frontal = models.FileField(editable=True)
    img_ci_posterior = models.FileField(editable=True)
    rsh = models.FileField(editable=True)
    direccion = models.CharField(max_length=500, editable=True)
    comuna = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    telefono = models.IntegerField(editable=True)
    curso = models.ForeignKey(Cursos,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    

    
