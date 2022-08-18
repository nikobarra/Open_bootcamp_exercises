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
    
    #obtener todos los elementos ordenados
    orders = Author.objects.all().order_by('email')
    
    #obtener todos los elementos cuyo id sea menor o igual a 15
    #__lte: menor o igual
    #__gte: mayor o igual
    #__lt: menor que
    #__gt: mayor que
    #__ne: diferente de
    #__in: pertenece a una lista
    #__contains: contiene una cadena
    #__icontains: contiene una cadena en mayusculas o minusculas
    #__startswith: empieza con una cadena
    #__istartswith: empieza con una cadena en mayusculas o minusculas
    #__endswith: termina con una cadena
    #__iendswith: termina con una cadena en mayusculas o minusculas
    #__isnull: es nulo
    
    filtered_2 = Author.objects.filter(id__lte=15)
    filtered_3=Author.objects.filter(name__contains = 'win')
    
    
    return render(request, 'post/queries.html',{'authors':authors, 'filtered':filtered, 'author':author, 'limits':limits, 'offsets':offsets, 'orders':orders, 'filtered_2':filtered_2, 'filtered_3':filtered_3})

