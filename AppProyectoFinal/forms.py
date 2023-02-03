from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PoliticaFM(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    localidad = forms.CharField(max_length=20)
    mail = forms.EmailField()

class SociedadFM(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    localidad = forms.CharField(max_length=20)
    mail = forms.EmailField()
    noticia = forms.CharField(
        max_length=600,
        widget=forms.Textarea(attrs={
            'class':'form-control',
            'style':'width: 500px; height: 50px; word-wrap: break-word; word-break: break-all'
        })
)

class DeporteFM(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    deporte = forms.CharField(max_length=20)
    club = forms.CharField(max_length=20)
    mail = forms.EmailField()

class InternacionalFM(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    pais = forms.CharField(max_length=25)
    mail = forms.EmailField()
    noticia = forms.CharField(
        max_length=600,
        widget=forms.Textarea(attrs={
            'class':'form-control',
            'style':'width: 500px; height: 50px; word-wrap: break-word; word-break: break-all'
        }))

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    # Obligatorios
    last_name = forms.CharField(label="Nombre:")
    first_name = forms.CharField(label="Apellido:")
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    

    class Meta:
        model = User
        fields = ['last_name', 'first_name','email', 'password1', 'password2']        

