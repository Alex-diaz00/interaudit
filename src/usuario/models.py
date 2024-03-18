from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models
import django_tables2 as tables

# Create your models here.

class Permiso(models.Model):
    nombre = models.CharField(max_length=500)
    estado = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        db_table = 'permiso'

    def __str__(self):
        return self.nombre


class Rol(models.Model):
    nombre = models.CharField(max_length=500)
    estado = models.BooleanField(default=True, verbose_name="Activo")
    id_permiso = models.ManyToManyField(Permiso, verbose_name='Permiso', related_name='roles')

    class Meta:
        db_table = 'rol'

    def __str__(self):
        return self.nombre



class Usuario(AbstractUser):
    username = models.CharField(max_length=100, unique=True, verbose_name='Usuario')
    password = models.CharField(max_length=100)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, db_column='id_rol',
                            blank=True, null=True)
    estado = models.BooleanField(default=True, verbose_name="Activo")

    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'usuario'


class FrecuenciaProcesamiento():
    hora = models.TimeField()

    class Frecuencia(models.TextChoices):
        diario = "Diario"
        semanal = "Semanal"
        mensual = "Mensual"

    frecuencia = models.CharField(max_length=7, choices=Frecuencia.choices, default=Frecuencia.diario)
    dia = models.PositiveIntegerField(default=10, validators=[MaxValueValidator(31)])

    class Meta:
        db_table = 'frecuencia'

