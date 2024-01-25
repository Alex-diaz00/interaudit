from django.conf import settings
from rest_framework.routers import DefaultRouter

import disposicion
import usuario
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
    path('insertar_permiso/', insertar_permiso, name='insertar_permiso'),

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
