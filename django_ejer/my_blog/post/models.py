
#usamos el paquete django-seed para crear una base de datos de prueba
#pip install django-seed
#pip install psycopg2-binary (si hay error al ejecutar el llenado de datos)
#luego agregamos al settings la app django_seed
#para llenar la bd de datos debemos ejeutar el comando: python manage.py seed nombre_app --number=15 (cantidad de elementos)

from django.db import models
from datetime import date

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name


class Entry(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    headline=models.CharField(max_length=255)
    body_text=models.TextField()
    public_date=models.DateField(default = date.today)
    rating = models.IntegerField(default = 5)
    
    def __str__(self):
        return self.headline
 

