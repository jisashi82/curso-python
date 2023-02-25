from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)

""" Ejecutar el comando-> py manage.py createsuperuser 
    para crear el superusuario del Panel de Administrador
"""