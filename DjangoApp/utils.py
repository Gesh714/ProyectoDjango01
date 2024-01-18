from docx import Document
from django.shortcuts import get_object_or_404
from .models import Inscrito

def reemplazar_marcadores(doc_path, inscrito_id):
    # Obtener el objeto Inscrito desde la base de datos
    inscrito = get_object_or_404(Inscrito, id=inscrito_id)

    # Abrir el documento existente
    doc = Document(doc_path)

    # Definir los marcadores que deseas buscar y reemplazar
    marcadores = {
        "[NOMBRE]": inscrito.nombre,
        "[RUT]": inscrito.rut,
        "[COMUNA]": inscrito.comuna,
        # Agrega más campos según sea necesario
    }

    # Iterar sobre los párrafos del documento
    for paragraph in doc.paragraphs:
        for marcador, valor in marcadores.items():
            # Reemplazar el marcador con el valor correspondiente
            paragraph.text = paragraph.text.replace(marcador, str(valor))

    # Guardar el documento modificado
    doc.save(doc_path)

# Ruta al documento original
ruta_documento_original = "documento_original.docx"

# Supongamos que queremos modificar el documento para el inscrito con id=1
inscrito_id_a_modificar = 1

# Llamada a la función para reemplazar marcadores
reemplazar_marcadores(ruta_documento_original, inscrito_id_a_modificar)