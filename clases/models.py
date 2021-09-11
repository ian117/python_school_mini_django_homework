from django.db import models

import uuid


class Clase(models.Model):
    nombre = models.CharField(max_length=200)
    horario_begin = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    horario_end = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
