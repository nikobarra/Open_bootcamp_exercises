from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

def test (request):
    return HttpResponse('funciona ok')


def create (request):
    #comment = Comment(name = 'Niko', score = 5, comment = 'Muy buen video')
    #comment.save()    
    comment = Comment.objects.create(name = 'Matias', comment = 'Muy buen video')
    return HttpResponse('creacion')

def delete (request):
    #comment = Comment.objects.get(id = 1)
    #comment.delete()
    Comment.objects.filter(id = 2).delete()
    return HttpResponse('borrado')
 