from django.shortcuts import render, redirect
from .forms import UploadExcelCursoForm, UploadExcelParticipantesForm, UploadExcelRelatorForm
import pandas as pd


# Create your views here.
def upload_participantes(request):
    if request.method == 'POST':
        form = UploadExcelParticipantesForm(request.POST, request.FILES)
        if form.is_valid():
            # Procesar el archivo excel aquí
            archivo_excel = form.cleaned_data['plantilla_participantes']
            # ... código para procesar el archivo y almacenar datos en la base de datos.
            return redirect('carga exitosa')
    else:
        form = UploadExcelParticipantesForm()

    return render(request, 'cargar_planillas/upload_participantes.html')

def upload_curso(request):
    if request.method == 'POST':
        form = UploadExcelCursoForm(request.POST, request.FILES)
        if form.is_valid():
            archivo_excel = form.cleaned_data['plantilla_curso']
            # Procesar el archivo excel aquí
            df = pd.read_excel(archivo_excel)
            # ... código para procesar el archivo y almacenar datos en la base de datos.
            return redirect('carga exitosa')
    else:
        form = UploadExcelCursoForm()

    return render(request, 'cargar_planillas/upload_curso.html')

def upload_relator(request):
    if request.method == 'POST':
        form = UploadExcelRelatorForm(request.POST, request.FILES)
        if form.is_valid():
            # Procesar el archivo excel aquí
            archivo_excel = form.cleaned_data['plantilla_relator']
            # ... código para procesar el archivo y almacenar datos en la base de datos.
            return redirect('carga exitosa')
    else:
        form = UploadExcelRelatorForm()

    return render(request, 'cargar_planillas/upload_relator.html')