from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant, Place

def create(request):
    place = Place(name='Lugar 1', address='Calle falsa 123')
    place.save()
    
    restaurant = Restaurant(place=place, number_of_employees=10)
    restaurant.save()
    return HttpResponse(restaurant.place.name)

