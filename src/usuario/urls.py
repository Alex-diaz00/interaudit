from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter(trailing_slash=False)
router.register(r'usuario', UsuarioView, basename='usuario_crud')
router.register(r'rol', RolView, basename='rol_crud')
router.register(r'permiso', PermisoView, basename='permiso_crud')

urlpatterns = [
    path('', include(router.urls), name="api"),

]
