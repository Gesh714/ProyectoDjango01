from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddCursoForm, AddParticipanteForm, UploadExcelCursoForm, UploadExcelParticipantesForm
from .models import Cursos_inscritos, Inscritos
from .utils import reemplazar_marcadores
from docx import Document
import pandas as pd

# Create your views here.
def home(request):

    return render(request, 'djangoapp/inicio.html', {})

def login_user(request):
    # check to see if loggin in
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Has ingresado con exito!")
            return redirect('login')
        else:
            messages.success(request, "Hubo un error en tu nombre de usuario y/o password. Intenta nuevamente.")
            return redirect('login')
        
    else:
         return render(request, 'djangoapp/login_user.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'Has finalizado sesion.')
    return redirect('inicio')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Te has registrado con exito! Bienvenido/a.")
			return redirect('inicio')
	else:
		form = SignUpForm()
		return render(request, 'djangoapp/register_user.html', {'form':form})

	return render(request, 'djangoapp/register_user.html', {'form':form})


def cargarCursosPlantilla(request):
	if request.method == 'POST':
		form = UploadExcelCursoForm(request.POST, request.FILES)
		if form.is_valid():
			curso = form.save()
			messages.success(request, "Inscrito exitosamente...")
			return redirect('ver_cursos')
		else:
			print(form.errors)
	else:
		form = UploadExcelParticipantesForm()

	return render(request, 'djangoapp/cargar_cursos_plantilla.html', {'form': form})

def cargarParticipantePlantilla(request):
    # Verifica si el usuario está autenticado
    if request.user.is_authenticated:
        # Verifica si la solicitud es POST y si se ha adjuntado un archivo Excel
        if request.method == 'POST' and request.FILES['archivo_excel']:
            archivo_excel = request.FILES['archivo_excel']

            try:
                # Utiliza pandas para leer el archivo Excel
                df = pd.read_excel(archivo_excel)

                # Itera sobre las filas y guarda los datos en la base de datos
                for _, row in df.iterrows():
                    inscrito = Inscritos(
                        nombre_completo = row['nombre completo'],
						rut = row['rut'],  # Assuming 'RUT' is a numeric field in the Excel
						fecha_nac = row['fecha de nacimiento'],
						sexo = row['sexo'],
						comuna = row['comuna'],
						escolaridad = row['codigo escolaridad'],
						pais_origen = row['pais origen'],
						direccion = row['direccion'],
						telefono = int(row['telefono']),
                    )
                    inscrito.save()

                messages.success(request, 'Datos de inscritos cargados exitosamente.')
                return redirect('pagina_exitosa')  # Redirige a una página de éxito

            except Exception as e:
                # Manejo de excepciones
                messages.error(request, f'Error al cargar los datos: {e}')

        return render(request, 'djangoapp/cargar_participante_plantilla.html', {})
        
    else:
        # Si el usuario no está autenticado, redirige a la página de inicio de sesión
        messages.success(request, "Debes iniciar sesión...")
        return redirect('login')

def extraerDatos(excel_file):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(excel_file)

    # Extract participant data
    data = []
    for _, row in df.iterrows():
        participant_data = {
            'nombre_completo': row['Nombre Completo'],
            'rut': row['RUT'],  # Assuming 'RUT' is a numeric field in the Excel
            'fecha_nac': row['Fecha de Nacimiento'],
            'sexo': row['Sexo'],
            'comuna': row['Comuna'],
            'escolaridad': row['Escolaridad'],
            'pais_origen': row['País Origen'],
            'direccion': row['Dirección'],
            'telefono': int(row['Teléfono']),
        }
        data.append(participant_data)

    return data

def verCursos(request):
    cursos = Cursos_inscritos.objects.all()
    return render(request, 'djangoapp/view_cursos.html', {'Cursos_inscritos':cursos})

def verParticipantes(request):
    inscritos = Inscritos.objects.all()
    return render(request, 'djangoapp/view_participantes.html', {'inscritos':inscritos})

def curso_info(request, pk):
	if request.user.is_authenticated:
		# Ver información de curso
		curso_data = Cursos_inscritos.objects.get(id=pk)
		return render(request, 'djangoapp/info_curso.html', {'curso_data':curso_data})
	else:
		messages.success(request, "Debes iniciar sesion...")
		return redirect('login')

def delete_curso(request, pk):
	if request.user.is_authenticated:
		delete_it = Cursos_inscritos.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Curso eliminado exitosamente...")
		return redirect('ver_cursos')
	else:
		messages.success(request, "Debes iniciar sesion...")
		return redirect('login')

def add_curso(request):
	form = AddCursoForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_curso = form.save()
				messages.success(request, "Curso registrado...")
				return redirect('ver_cursos')
		return render(request, 'djangoapp/cargar_cursos_manual.html', {'form':form})
	else:
		messages.success(request, "Debes iniciar sesion...")
		return redirect('login')


def participante_info(request, pk):
	if request.user.is_authenticated:
		# Ver información de participante
		inscrito_data = Inscritos.objects.get(id=pk)
		return render(request, 'djangoapp/info_participante.html', {'inscrito_data':inscrito_data})
	else:
		messages.success(request, "Debes iniciar sesion...")
		return redirect('login')

def delete_participante(request, pk):
	if request.user.is_authenticated:
		delete_it = Inscritos.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Inscrito eliminado exitosamente...")
		return redirect('ver_cursos')
	else:
		messages.success(request, "Debes iniciar sesion...")
		return redirect('login')

def add_participante(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddParticipanteForm(request.POST, request.FILES)
            if form.is_valid():
                participante = form.save()
                messages.success(request, "Inscrito exitosamente...")
                return redirect('ver_participantes')
            else:
                print(form.errors)
        else:
            form = AddParticipanteForm()
        return render(request, 'djangoapp/cargar_participante_manual.html', {'form': form})
    else:
        messages.success(request, "Debes iniciar sesión...")
        return redirect('login')

def update_curso(request, pk):
	if request.user.is_authenticated:
		current_curso = Cursos_inscritos.objects.get(id=pk)
		form = AddCursoForm(request.POST or None, instance=current_curso)
		if form.is_valid():
			form.save()
			messages.success(request, "El registro ha sido modificado!")
			return redirect('ver_cursos')
		return render(request, 'djangoapp/modificar_curso.html', {'form':form})
	else:
		messages.success(request, "Debes iniciar sesion...")
		return redirect('login')

def update_participante(request, pk):
	if request.user.is_authenticated:
		current_participante = Inscritos.objects.get(id=pk)
		form = AddParticipanteForm(request.POST or None, instance=current_participante)
		if form.is_valid():
			form.save()
			messages.success(request, "El registro ha sido modificado!")
			return redirect('ver_participantes')
		return render(request, 'djangoapp/modificar_participante.html', {'form':form})
	else:
		messages.success(request, "Debes iniciar sesion...")
		return redirect('login')
	
def crear_documentos(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # Aquí debes realizar la lógica para obtener los inscritos que deseas procesar
            # Puedes obtener los IDs de los inscritos desde el formulario o cualquier otra fuente
            lista_de_inscritos_a_procesar = [1, 2, 3]  # Ejemplo, reemplaza con tu lógica

            # Ruta al documento original
            ruta_documento_original = "documento_original.docx"

            # Procesar cada inscrito
            for inscrito_id in lista_de_inscritos_a_procesar:
                try:
                    # Llamada a la función para reemplazar marcadores
                    reemplazar_marcadores(ruta_documento_original, inscrito_id)
                    messages.success(request, f'Documento para inscrito {inscrito_id} creado exitosamente.')
                except Exception as e:
                    messages.error(request, f'Error al crear documento para inscrito {inscrito_id}: {e}')

            # Puedes redirigir a una página de éxito o renderizar la misma página con un mensaje
            return render(request, 'djangoapp/crear_documentos.html', {'exito': True})

        return render(request, 'djangoapp/crear_documentos.html', {})

    else:
        messages.success(request, "Debes iniciar sesión...")
        return redirect('login')