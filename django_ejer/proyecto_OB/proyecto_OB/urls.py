
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', views.saludo, name='saludo'),
    path ('despedida/', views.despedida, name='despedida'),
    #path ('', views.index, name='index'),
    path ('adulto/<int:edad>/', views.adulto, name='adulto'),
]
