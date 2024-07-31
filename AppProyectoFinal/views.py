from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.template import loader
from django.template import Template, context

from AppProyectoFinal.forms import PoliticaFM, InternacionalFM, DeporteFM, SociedadFM
from AppProyectoFinal.models import Politica, Sociedad, Deporte, Internacional
from AppProyectoFinal import models
from AppProyectoFinal.forms import UserRegisterForm
from AppProyectoFinal.forms import UserRegisterForm, UserEditForm

from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def inicio(request):
    return render(request, "AppProyectoFinal/inicio.html")


@login_required
def politica(request):
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = PoliticaFM(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            politica = Politica(nombre=informacion['nombre'], apellido=informacion['apellido'],
                                localidad=informacion['localidad'], mail=informacion['mail'])
            politica.save()
            # Vuelvo al inicio o a donde quieran
            return render(request, "AppProyectoFinal/inicio.html")
    else:
        miFormulario = PoliticaFM()  # Formulario vacio para construir el html

    return render(request, "AppProyectoFinal/politica.html", {"miFormulario": miFormulario})


@login_required
def sociedad(request):
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = SociedadFM(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            sociedad = Sociedad(nombre=informacion['nombre'], apellido=informacion['apellido'],
                                localidad=informacion['localidad'], mail=informacion['mail'], noticia=informacion['noticia'])
            sociedad.save()
            # Vuelvo al inicio o a donde quieran
            return render(request, "AppProyectoFinal/inicio.html")
    else:
        miFormulario = SociedadFM()  # Formulario vacio para construir el html

    return render(request, "AppProyectoFinal/sociedad.html", {"miFormulario": miFormulario})


@login_required
def deporte(request):
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = DeporteFM(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            deporte = Deporte(nombre=informacion['nombre'], apellido=informacion['apellido'],
                              deporte=informacion['deporte'], club=informacion['club'], mail=informacion['mail'])
            deporte.save()
            # Vuelvo al inicio o a donde quieran
            return render(request, "AppProyectoFinal/inicio.html")
    else:
        miFormulario = DeporteFM()  # Formulario vacio para construir el html

    return render(request, "AppProyectoFinal/deporte.html", {"miFormulario": miFormulario})


@login_required
def internacional(request):
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = InternacionalFM(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            internacional = Internacional(nombre=informacion['nombre'], apellido=informacion['apellido'],
                                          pais=informacion['pais'], noticia=informacion['noticia'], mail=informacion['mail'])
            internacional.save()
            # Vuelvo al inicio o a donde quieran
            return render(request, "AppProyectoFinal/inicio.html")
    else:
        miFormulario = InternacionalFM()  # Formulario vacio para construir el html

    return render(request, "AppProyectoFinal/internacional.html", {"miFormulario": miFormulario})

# def index(request):
    # return render(request, 'AppProyectoFinal/index.html')


def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppProyectoFinal/inicio.html", {"mensaje": f"Bienvenido {usuario}"})

            else:
                form = AuthenticationForm()
                return render(request, "AppProyectoFinal/login.html", {"mensaje": "Datos incorrectos"}, {"form": form})

        else:

            return render(request, "AppProyectoFinal/login.html", {"form": form, "mensaje": "Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppProyectoFinal/login.html", {"form": form})


def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return redirect("/AppProyectoFinal/login")

    else:
        form = UserCreationForm()
        form = UserRegisterForm()

    return render(request, "AppProyectoFinal/registro.html",  {"form": form})


def inicio(request):

    return render(request, "AppProyectoFinal/inicio.html")


@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.set_password(informacion['password1'])
            usuario.email = informacion['email']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()

            return render(request, "AppProyectoFinal/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppProyectoFinal/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})


class SociedadList(ListView):

    model = Sociedad
    template_name = "AppProyectoFinal/sociedad_list.html"


class SociedadDetalle(DetailView):

    model = Sociedad
    template_name = "AppProyectoFinal/sociedad_detalle.html"


class SociedadCreacion(CreateView):

    model = Sociedad
    success_url = "/AppProyectoFinal/sociedad/list"
    fields = ['nombre', 'noticia']


class SociedadUpdate(UpdateView):

    model = Sociedad
    success_url = "/AppProyectoFinal/sociedad/list"
    fields = ['nombre', 'noticia']


class SociedadDelete(DeleteView):

    model = Sociedad
    success_url = "/AppProyectoFinal/sociedad/list"


def buscar(request):
    localidad = request.GET.get('localidad')
    if localidad:
        noticias = Sociedad.objects.filter(localidad__iexact=localidad)
    else:
        noticias = []
    return render(request, 'AppProyectoFinal/inicio.html', {'noticias': noticias})


def nosotros(request):
    return render(request, "AppProyectoFinal/nosotros.html")


def nada(request):
    return render(request, "AppProyectoFinal/nada.html")
