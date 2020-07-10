from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('create_comment/',login_required(CreateComment.as_view()), name='create_comment'),
    path('list_comment/',login_required(ListComment.as_view()), name='list_comment'),
    path('edit_comment/<int:pk>/', login_required(UpdateComment.as_view()), name= 'update_comment'),
    path('delete_comment/<int:pk>/', login_required(DeleteComment.as_view()), name= 'delete_comment'),

#    path('listas_libros/', login_required(ListadoLibros.as_view()), name = 'listado_libros'),
#    path('crear_libro/', login_required(CrearLibro.as_view()), name = 'crear_libro'),
#    path('editar_libro/<int:pk>/', login_required(ActualizarLibro.as_view()), name = 'editar_libro'),
#    path('eliminar_libro/<int:pk>/', login_required(EliminarLibro.as_view()), name = 'eliminar_libro')

]