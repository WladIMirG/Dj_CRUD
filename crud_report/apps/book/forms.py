from  django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','publications_date','state']
        label = {
            'title':'Título del libro',
            'publications_date': 'Fecha de Publciación del Libro',
            'state':'Estado del libro',
        }
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese título de libro'
                }
            ),
            'publications_date': forms.SelectDateWidget(
#                attrs = {
#                    'class': 'form-control'
#                }
            )
        }
