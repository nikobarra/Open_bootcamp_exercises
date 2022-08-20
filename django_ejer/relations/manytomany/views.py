from django.shortcuts import render
from django.http import HttpResponse
from .models import Publication, Article


def create(request):
    """ art1=Article(headline='headline art 1')
    art1.save()
    art2=Article(headline='headline art 2')
    art2.save()
    art3=Article(headline='headline art 3')
    art3.save()
    
    pub1 = Publication(title='publication 1')
    pub1.save()
    pub2 = Publication(title='publication 2')
    pub2.save()
    pub3 = Publication(title='publication 3')
    pub3.save()
    pub4 = Publication(title='publication 4')
    pub4.save()
    pub5 = Publication(title='publication 5')
    pub5.save()
    pub6 = Publication(title='publication 6')
    pub6.save()
    pub7 = Publication(title='publication 7')
    pub7.save()
    
    # antes de realcionar los articulos con las publicaciones deben estar todos guardados
    
    art1.publications.add(pub1, pub2, pub3)
    art2.publications.add(pub4, pub5)
    art3.publications.add(pub6, pub7) """
    
    #resultado = art1.publications.all()
    # art1.publications.remove(pub1)
    pub1 = Publication.objects.get(id=1)
    resultado = pub1.article_set.all()
    return HttpResponse(resultado)


