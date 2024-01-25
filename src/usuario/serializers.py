from rest_framework import serializers
from .models import Usuario, Rol, Permiso, FrecuenciaProcesamiento
from rest_framework.validators import *

class UsuarioAllFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ["password"]
        extra_kwargs = {
        'password': {
            'write_only': True,
            'style': {'input_type': 'password'}
        }
        }

    def validar_usuario(self, usuario):

        if not usuario.get("username"):
            raise ValidationError("El nombre de usuario no debe estar vacío")
        if not usuario.get('password'):
            raise ValidationError("La contraseña de usuario no debe estar vacía")

        if Usuario.objects.filter(username=usuario.get("username")).exists():
            raise ValidationError("Nombre de usuario existente")

    def create(self, validated_data):

        name = validated_data.pop('username', None)
        password = validated_data.pop('password', None)

        instance = self.Meta.model(**validated_data)
        instance.username = name
        instance.set_password(password)
        instance.save()
        return instance


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'


class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = "__all__"

class FrecuenciaProcesamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrecuenciaProcesamiento
        fields = "__all__"