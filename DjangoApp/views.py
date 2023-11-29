from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddCursoForm, AddParticipanteForm
from .models import Cursos_inscritos, Inscritos

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

    return render(request, 'djangoapp/cargar_cursos_plantilla.html', {})

def cargarParticipantePlantilla(request):

    return render(request, 'djangoapp/cargar_participante_plantilla.html', {})

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
	form = AddParticipanteForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_participante = form.save()
				messages.success(request, "Inscrito exitosamente...")
				return redirect('ver_participantes')
		return render(request, 'djangoapp/cargar_participante_manual.html', {'form':form})
	else:
		messages.success(request, "Debes iniciar sesion...")
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