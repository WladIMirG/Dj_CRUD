from  django import forms
from .models import Book, Comment

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','publications_date']
#        label = {
#            'titulo':'Título del libro',
#            'fecha_publicacion': 'Fecha de Publciación del Libro'
#        }
#        widgets = {
#            'titulo': forms.TextInput(
#                attrs = {
#                    'class': 'form-control',
#                    'placeholder': 'Ingrese título de libro'
#                }
#            ),
#            'autor_id': forms.SelectMultiple(
#                attrs = {
#                    'class':'form-control'
#                }
#            ),
#            'fecha_publicacion': forms.SelectDateWidget(
#                attrs = {
#                    'class': 'form-control'
#                }
#            )
#        }