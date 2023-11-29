from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Cursos_inscritos, Inscritos

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

# Create Add Curso Form
class AddCursoForm(forms.ModelForm):
	nombre_curso = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nombre del Curso", "class":"form-control"}), label="")
	id_sence = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"ID Sence", "class":"form-control"}), label="")
	comuna = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Comuna", "class":"form-control"}), label="")
	region = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Region", "class":"form-control"}), label="")
	fecha_inicio = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Fecha de inicio", "class":"form-control"}), label="")
	fecha_termino = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Fecha de termino", "class":"form-control"}), label="")
	modalidad = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Modalidad", "class":"form-control"}), label="")

	class Meta:
		model = Cursos_inscritos
		fields = ('nombre_curso', 'id_sence', 'comuna', 'region', 'fecha_inicio', 'fecha_termino', 'modalidad')

class AddParticipanteForm(forms.ModelForm):
	nombre_completo = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nombre Participante", "class":"form-control"}), label="")
	rut = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Rut", "class":"form-control"}), label="")
	fecha_nac = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"placeholder":"Fecha de Nac", "class":"form-control"}), label="")
	genero = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Genero", "class":"form-control"}), label="")
	img_ci_frontal = forms.FileField(required=True, widget=forms.widgets.FileInput(attrs={"class":"form-control"}), label="")
	img_ci_posterior = forms.FileField(required=True, widget=forms.widgets.FileInput(attrs={"class":"form-control"}), label="")
	rsh = forms.FileField(required=True, widget=forms.widgets.FileInput(attrs={"class":"form-control"}), label="")
	direccion = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Direccion", "class":"form-control"}), label="")
	comuna = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Comuna", "class":"form-control"}), label="")
	region = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Region", "class":"form-control"}), label="")
	telefono = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Telefono", "class":"form-control"}), label="")
	curso = forms.ModelChoiceField(required=True, queryset=Cursos_inscritos.objects.all(), empty_label=None, widget=forms.widgets.ChoiceWidget(attrs={"class":"form-control"}), label="")

	class Meta:
		model = Inscritos
		fields = (
			'nombre_completo',
			'rut',
			'fecha_nac',
			'genero',
			'img_ci_frontal',
			'img_ci_posterior',
			'rsh',
			'direccion',
			'comuna',
			'region',
			'telefono',
			'curso',
			)