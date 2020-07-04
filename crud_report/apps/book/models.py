from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    id_book = models.AutoField(primary_key = True)
    title = models.CharField('Titulo', max_length = 200, blank=False, null=False)
    publications_date = models.DateField('Fecha de Publicacion', blank=False, null=False)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['title']
        
    def __str__(self):
        return self.title

class Comment(models.Model):
    id_comment = models.AutoField(primary_key = True)
    id_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    #id_user = models.ForeignKey(User.username., on_delete=models.CASCADE)
    text = models.TextField(max_length=255, blank=False)
    created_date = models.DateTimeField('Fecha de creacion', auto_now_add=True)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return 'Comentario '+str(self.id_comment)+' para '+str(self.id_book)