from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date

def create(request):
    rep = Reporter(first_name='Niko', last_name='Barra', email='niko@niko.com')
    rep.save()
    
    art1 = Article(headline='primer articulo', pub_date=date(2022,7,20), reporter = rep)
    art1.save()
    art2 = Article(headline='segundo articulo', pub_date=date(2022,6,15), reporter = rep)
    art2.save()
    art3 = Article(headline='tercer articulo', pub_date=date(2021,3,10), reporter = rep)
    art3.save()
    
    #result = art1.reporter.first_name
    result = rep.article_set.all()
    return HttpResponse(result)