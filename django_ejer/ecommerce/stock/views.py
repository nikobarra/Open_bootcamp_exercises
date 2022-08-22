from django.shortcuts import render
from .forms import ProductForm
from django.http import HttpResponseRedirect

def index(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ProductForm()
        return render (request, 'index.html',{'form': form})

