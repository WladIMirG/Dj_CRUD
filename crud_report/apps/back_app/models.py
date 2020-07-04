from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class User(AbstractBaseUser):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creacion"
    )

#class Books(models.Model):
#    id_book = models.AutoField(primary_key = True)
#    title = models.CharField(max_length = 200,)
#    publications_date = models.DateField('%m/%d/%Y')
    

#class Comments(models.Model):
#    id_comment = models.AutoField(primary_key = True)
#    id_book = models.ForeignKey(Books, on_delete=models.CASCADE)
#    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
#    text = models.TextField(max_length=255, blank=False)
#    created_date = models.DateTimeField('%m/%d/%Y %H:%M:%S', auto_now_add=True)
    