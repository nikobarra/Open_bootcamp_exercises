from django.db import models
#En este ejercicio tendrás que crear una aplicación en Django que almacene datos de directores de cine y luego se puedan ver sus películas, así como una descripción de las mismas.
#Tienes que personalizar el admin de la aplicación y a su vez crear las vistas de cada una de las partes de la aplicación.

class Directores(models.Model):
    name = models.CharField(max_length=60, help_text='Nombre del director')
    
    def __str__(self) -> str:
        return self.name
    
class Movies(models.Model):
    name = models.CharField(max_length=60, help_text='Nombre de la película')
    director = models.ForeignKey(Directores, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=200, help_text='Descripción de la película')
    year = models.IntegerField(help_text='Año de la película')
    image = models.ImageField(upload_to='movies', help_text='Imagen de la película')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name