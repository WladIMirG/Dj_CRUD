from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import BookForm

def Home(request):
    return render(request, 'index.html')


def CreateBook(request):
    print('ENTRE AL METODO CreateBook',request.method)
    if request.method == 'POST':
        print('ENTRO Y LA RESPUESTA ES POST')
        Book_Form = BookForm(request.POST)
        if Book_Form.is_valid:
            Book_Form.save()
            return redirect('index')
    else:
        print('ENTRO SIEMPRE AL SINO')
        Book_Form = BookForm()

    return render(request, 'book/create_book.html',{'Book_form':Book_Form})

# Create your views here.
