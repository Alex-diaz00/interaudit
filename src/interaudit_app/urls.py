from django.conf import settings
from rest_framework.routers import DefaultRouter

import disposicion
import usuario
from categoria.views import insertar_categoria, delete_categoria, delete_subcategoria, insertar_subcategoria, \
    edicion_subcategoria, editar_subcategoria, edicion_categoria, editar_categoria
from usuario import urls
from home.views import CustomSignupView
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from disposicion import urls

from usuario.views import UsuarioView, RolView, PermisoView
from allauth.account import urls
from usuario.views import *
router = DefaultRouter(trailing_slash=False)



urlpatterns = [
    path('', include(router.urls), name="api"),
    path('', include(usuario.urls)),
    path('', include(disposicion.urls)),
    # path('table/usuario', UsuarioTView.as_view(), name="table"),
    # path("usuario/<int:pk>/", UsuarioView.as_view({'delete': 'destroy'}), name="delete_user"),
    path('delete_user/<int:id>', delete_user, name="delete_user"),
    path('delete_permiso/<int:id>', delete_permiso, name="delete_permiso"),
    path('delete_rol/<int:id>', delete_rol, name="delete_rol"),
    path('delete_categoria/<int:id>', delete_categoria, name="delete_categoria"),
    path('delete_subcategoria/<int:id>', delete_subcategoria, name="delete_subcategoria"),
    path('insertar_permiso/', insertar_permiso, name='insertar_permiso'),
    path('insertar_rol/', insertar_rol, name='insertar_rol'),
    path('insertar_usuario/', insertar_usuario, name='insertar_usuario'),
    path('insertar_categoria/', insertar_categoria, name='insertar_categoria'),
    path('insertar_subcategoria/', insertar_subcategoria, name='insertar_subcategoria'),


    path('edicion_usuario/<int:id>', edicion_usuario, name='edicion_usuario'),
    path('editar_usuario/', editar_usuario, name='editar_usuario'),
    path('edicion_rol/<int:id>', edicion_rol, name='edicion_rol'),
    path('editar_rol/', editar_rol, name='editar_rol'),
    path('edicion_permiso/<int:id>', edicion_permiso, name='edicion_permiso'),
    path('editar_permiso/', editar_permiso, name='editar_permiso'),
    path('edicion_subcategoria/<int:id>', edicion_subcategoria, name='edicion_subcategoria'),
    path('editar_subcategoria/', editar_subcategoria, name='editar_subcategoria'),
    path('edicion_categoria/<int:id>', edicion_categoria, name='edicion_categoria'),
    path('editar_categoria/', editar_categoria, name='editar_categoria'),
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('accounts/', include('allauth.urls')),
    path("accounts/signup_user/", CustomSignupView.as_view(), name="signup_user"),
    # path('api-auth/', include('rest_framework.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/doc/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]



if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
