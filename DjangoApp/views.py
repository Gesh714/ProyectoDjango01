from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

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

def cargarCursosManual(request):

    return render(request, 'djangoapp/cargar_cursos_manual.html', {})

def cargarParticipantePlantilla(request):

    return render(request, 'djangoapp/cargar_participante_plantilla.html', {})

def cargarParticipanteManual(request):

    return render(request, 'djangoapp/cargar_participante_manual.html', {})

def verCursos(request):

    return (request, 'djangoapp/view_cursos.html', {})

def verParticipantes(request):

    return (request, 'djangoapp/view_participantes.html', {})
