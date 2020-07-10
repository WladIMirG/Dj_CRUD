from  django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['id_book', 'user', 'text',]
        label = {
            'id_book':'ID del libro',
            'user': 'ID usuario',
            'text':'texto del comentario',
            'created_date':'Fecha de creacion',
        }
        widgets = {
            'id_book': forms.Select(
                attrs = {
#                    'class':'form-control'
                }
            ),
            'id_book': forms.Select(
                attrs = {
#                    'class':'form-control'
                }
            ),
            'text': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese su comentario',
#                    'id':'descripcion'
                }
            ),
        }