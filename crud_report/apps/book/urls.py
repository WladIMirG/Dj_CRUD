from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('create_book/', login_required(CreateBook.as_view()), name='create_book'),
    path('list_book/', login_required(ListBook.as_view()), name='list_book'),
    path('edit_book/<int:pk>/', login_required(UpdateBook.as_view()), name= 'update_book'),
    path('delete_book/<int:pk>/', DeleteBook.as_view(), name= 'delete_book'),
]