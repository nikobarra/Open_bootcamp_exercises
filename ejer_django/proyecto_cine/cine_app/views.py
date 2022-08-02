from django.shortcuts import render

from .models import Directores, Movies


def index(request):
    num_movies = Movies.objects.all().count()
    cant_directores = Directores.objects.all().count()
    
    return render(request, 'cine_app/index.html', context={
        'num_movies': num_movies, 
        'cant_directores': cant_directores
        })
    