from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email =  models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address =  models.CharField(max_length=100)
    city =  models.CharField(max_length=50)
    state =  models.CharField(max_length=50)
    zipcode =  models.CharField(max_length=20)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    

class Cursos_inscritos(models.Model):
    modalidades = models.TextChoices("Modalidades","Presencial e-learning")

    nombre_curso = models.CharField(max_length=200)
    id_sence = models.IntegerField()
    comuna = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    fecha_inicio = models.CharField(max_length=10)
    fecha_termino = models.CharField(max_length=10)
    modalidad = models.CharField(blank=True, choices=modalidades.choices, max_length=10)

    def __str__(self):
        return self.nombre_curso
    
class Inscritos(models.Model):
    nombre_completo = models.CharField(max_length=200,null=True)
    rut = models.CharField(max_length=10,null=True)
    fecha_nac = models.DateField(null=True)
    sexo = models.CharField(max_length=100,null=True)
    img_ci_frontal = models.FileField(upload_to='archivos_participantes/', verbose_name='Imagen frontal del CI', name='img_field_frontal', error_messages="Sobrescribiendo",null=True)
    img_ci_posterior = models.FileField(upload_to='archivos_participantes/', verbose_name='Imagen posterior del CI', name='img_field_posterior', error_messages="Sobrescribiendo",null=True)
    rsh = models.FileField(upload_to='archivos_participantes/', verbose_name='Registro social de hogares', name='rsh', error_messages="Sobrescribiendo",null=True)
    escolaridad = models.CharField(max_length=10, null=True)
    pais_origen = models.CharField(max_length=80,null=True)
    direccion = models.CharField(max_length=500,null=True)
    comuna = models.CharField(max_length=200,null=True)
    region = models.CharField(max_length=200,null=True)
    telefono = models.IntegerField(null=True)
    curso = models.ForeignKey(Cursos_inscritos,on_delete=models.CASCADE,null=True)

    def __str__(self) -> str:
        return self.nombre_completo
        

    
    


    


    

    
