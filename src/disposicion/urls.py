from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter(trailing_slash=False)
router.register(r'gaceta', GacetaOficialView, basename='usuario_crud')
router.register(r'emisor', EmisorView, basename='rol_crud')
router.register(r'tipo-disposicion-funcion', TipoDisposicionFuncionView, basename='permiso_crud')
router.register(r'tipo-disposicion-emite', TipoDisposicionEmiteView, basename='usuario_crud')
router.register(r'tipo-disposicion-estado', TiempoDisposicionEstadoView, basename='rol_crud')
router.register(r'estado-disposicion', EstadoDisposicionView, basename='permiso_crud')
router.register(r'disposicion', DisposicionView, basename='usuario_crud')
router.register(r'nota-cambio', NotaCambioView, basename='rol_crud')


urlpatterns = [
    path('', include(router.urls), name="api"),

]
