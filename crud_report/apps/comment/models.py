from django.db import models

class Comment(models.Model):
    id_comment = models.AutoField(primary_key = True)
    id_book = models.ForeignKey('book.Book', on_delete=models.CASCADE)
    user = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
    text = models.TextField(max_length=255, blank=False)
    created_date = models.DateTimeField('Fecha de creacion', auto_now_add=True)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return 'Comentario '+str(self.id_comment)+': de '+str(self.user)+' para '+str(self.id_book)

        