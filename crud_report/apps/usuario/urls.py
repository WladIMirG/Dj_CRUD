from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from apps.usuario.views import InicioUsuarios,ListadoUsuario, RegistrarUsuario,EditarUsuario,EliminarUsuario

urlpatterns = [
    path('inicio/', InicioUsuarios.as_view(), name='inicio_usuarios'),
    path('listado/', ListadoUsuario.as_view(),{'parametro_extra': 'Hola!'},name='listar_usuarios'),
    path('registrar/',RegistrarUsuario.as_view(),name = 'registrar_usuario'),
    path('actualizar/<int:pk>/',EditarUsuario.as_view(), name = 'actualizar_usuario'),
    path('eliminar/<int:pk>/',EliminarUsuario.as_view(), name='eliminar_usuario'),
]
