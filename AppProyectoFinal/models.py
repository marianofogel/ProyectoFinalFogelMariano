from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Politica(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    localidad = models.CharField(max_length=10)
    mail = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Localidad: {self.localidad} - POLÍTICA"

class Sociedad(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    localidad = models.CharField(max_length=10)
    mail = models.EmailField()
    noticia = models.CharField(max_length=300)

    def __str__(self):
        return f"Nombre: {self.nombre} - Localidad: {self.localidad} - SOCIEDAD"

class Deporte(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    deporte = models.CharField(max_length=30)
    club = models.CharField(max_length=20)
    mail = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Deporte: {self.deporte} - DEPORTE"

class Internacional(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    pais = models.CharField(max_length=25)
    mail = models.EmailField()
    noticia = models.CharField(max_length=300)

    def __str__(self):
        return f'Nombre: {self.nombre} - País: {self.pais} - INTERNACIONAL'

