from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self) -> str:
        return self.title


"""
1.-Preparar la migracion con el comando-> py manage.py makemigrations blog 
   esto genera el archivo 0001_initial.py en la carpeta  migrations
2.-Visualizar  el SQL con el comando-> py manage.py sqlmigrate blog 0001
3.-Realizar la migracion con el comando-> py manage.py migrate blog
"""