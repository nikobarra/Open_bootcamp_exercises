
from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm, ContactForm

def form(request):
    comment_form =CommentForm({'name':'Juan', 'url':'http://www.google.com', 'comment':'Hola mundo'})
    return render(request, 'form.html', {'form': comment_form})


def goal(request):
    if request.method != 'POST':
        return HttpResponse('Metodo no permitido')
    
    return HttpResponse(request.POST['name'])


def widget(request):
#usamos el get y el post en una misma vista!, el get para mostrar el formulario y el post para recibir info
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'widget.html', {'form': form})

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse('Valido POST')
        else:
            return render(request, 'widget.html', {'form': form}) #muestra el error al usuario
     

    