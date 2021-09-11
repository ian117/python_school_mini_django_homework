from django.db import models
import uuid

# Create your models here.
from clases.models import Clase


class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    edad = models.IntegerField()
    activo = models.BooleanField(default=True)
    clases = models.ManyToManyField(Clase, blank=True)

    def __str__(self):
        return self.nombre
