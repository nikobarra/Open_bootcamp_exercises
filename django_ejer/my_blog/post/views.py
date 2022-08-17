from django.shortcuts import render
from .models import Author, Entry

def queries(request):
    #obtener todos los autores
    authors = Author.objects.all()
    
    #obtener datos filtrados por condicion
    filtered = Author.objects.filter(email ='tyler03@example.com')
    
    #obterner un unico objeto
    
    author = Author.objects.get(id=1)
    
    #busqueda con limites por ejemplo 10 primeros registros
    limits = Author.objects.all()[:10]
    
    #busqueda con offset (comenzar desde/hasta un punto especifico slicing)
    offsets = Author.objects.all()[5:10]
    
    return render(request, 'post/queries.html',{'authors':authors, 'filtered':filtered, 'author':author, 'limits':limits, 'offsets':offsets})

