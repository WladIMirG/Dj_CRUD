from django.urls import path
#from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('create_book/',CreateBook, name='create_book')
]