from django.urls import path
from django.contrib.auth import views as auth_views

from categoria.views import CategoriaTView, SubcategoriaTView
from disposicion.views import TipoDisposicionFuncionTView, TipoDisposicionEmiteTView, EstadoDisposicionTView, \
    EmisorTView
from usuario.views import UsuarioTView, PermisoTView, RolTView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('tables/', views.tables, name='tables'),
    path('usuarios/', UsuarioTView.as_view(), name='usuarios'),
    path('permisos/', PermisoTView.as_view(), name='permisos'),
    path('roles/', RolTView.as_view(), name='roles'),
    path('categorias/', CategoriaTView.as_view(), name='categorias'),
    path('subcategorias/', SubcategoriaTView.as_view(), name='subcategorias'),
    path('tipo-disposicion-funcion/', TipoDisposicionFuncionTView.as_view(), name='tipo-disposicion-funcion'),
    path('tipo-disposicion-emite/', TipoDisposicionEmiteTView.as_view(), name='tipo-disposicion-emite'),
    path('estado-disposicion/', EstadoDisposicionTView.as_view(), name='estado-disposicion'),
    path('emisor/', EmisorTView.as_view(), name='emisor'),


    path('vr/', views.vr, name='vr'),
    path('billing/', views.billing, name='billing'),
    path('rtl/', views.rtl, name='rtl'),
    path('profile/', views.profile, name='profile'),

        # Authentication
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/register/', views.UserRegistration.as_view(), name='register'),
    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name="password_change_done"),
    path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
]
