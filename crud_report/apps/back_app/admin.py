from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User)
class UserAdmin(UserAdmin):
    pass


#admin.site.register(Books)
#admin.site.register(Comments)
# Register your models here.
