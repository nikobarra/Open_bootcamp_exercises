from django.shortcuts import render

def simple(request):
    return render(request, 'simple.html')

def dinamico(request, name):
    categories = ['categoria1', 'categoria2', 'categoria3']
    context = {'name':name, 'categories':categories}
    return render(request, 'dinamico.html', context)