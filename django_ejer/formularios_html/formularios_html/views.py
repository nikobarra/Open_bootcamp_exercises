from django.shortcuts import render
from django.http import HttpResponse

def getform(request):
    return render(request, 'forms/form.html',{})


def getgoal(request):
    if request.method != 'GET':
        return HttpResponse('<h1>no es metodo get</h1>')
    
    name = request.GET.get('nombre')
    return render(request, 'forms/sucess.html',{'name':name})

def postform(request):
    return render (request, 'forms/postform.html',{})

def postgoal(request):
    if request.method != 'POST':
        return HttpResponse('<h1>no es metodo post</h1>')

    info = request.POST['info']
    return render(request, 'forms/postsuccess.html',{'info':info})