from django.db import models
#from django.contrib.auth.models import User

class Book(models.Model):
    id_book = models.AutoField(primary_key = True)
    id_comment=models.ManyToManyField('comment.Comment')
    title = models.CharField('Titulo', max_length = 200, blank=False, null=False)
    publications_date = models.DateField('Fecha de Publicacion', blank=False, null=False)
    state = models.BooleanField(default = True, verbose_name = 'Estado')
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Libros'
        ordering = ['id_book']
        
    def __str__(self):
        return self.title

        