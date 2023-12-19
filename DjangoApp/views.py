from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddCursoForm, AddParticipanteForm, UploadExcelCursoForm, UploadExcelParticipantesForm
from .models import Cursos_inscritos, Inscritos
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
	if request.method == 'POST':
		form = UploadExcelParticipantesForm(request.POST, request.FILES)
		if form.is_valid():
			excel_file = form.cleaned_data['file']
			data = extraerDatos(excel_file)
			# Aquí puedes utilizar la lista de diccionarios 'data' para llenar el formulario
			# o realizar cualquier otra acción que necesites con los datos extraídos del archivo de Excel
		
	return render(request, 'djangoapp/cargar_participante_plantilla.html', {'form': form})

def extraerDatos(excel_file):
	# Lee el archivo de Excel y almacena el resultado en un DataFrame
    df = pd.read_excel(excel_file)

    # Extrae los datos que necesitas de la hoja de cálculo
    data = []
    for index, row in df.iterrows():
        data.append({
            'column1': row['Column1'],
            'column2': row['Column2'],
            'column3': row['Column3'],
            'column4': row['column4'],
            'column5': row['Column5'],
            'column6': row['Column6'],
            'column7': row['Column7'],
            'column8': row['Column8'],
            'column9': row['Column9'],
        })

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