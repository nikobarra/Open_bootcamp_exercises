from django.shortcuts import render
from django.http import HttpResponse

def form(request):
    return render(request, 'form.html',{})


def goal(request):
    if request.method != 'GET':
        return HttpResponse('<h1>no es metodo get</h1>')
    
    name = request.GET.get('nombre')
    return render(request, 'sucess.html',{'name':name})