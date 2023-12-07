from django import forms

class UploadExcelParticipantesForm(forms.Form):
    archivo_excel = forms.FileField()

class UploadExcelCursoForm(forms.Form):
    archivo_excel = forms.FileField()

class UploadExcelRelatorForm(forms.Form):
    archivo_excel = forms.FileField()

