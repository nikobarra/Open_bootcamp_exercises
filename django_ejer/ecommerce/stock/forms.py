from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'short_description', 'description', 'stock', 'price']
        labels = {
            'name': 'Product Name',
            'short_description': 'Short Description',
            'description': 'Description',
            'stock': 'Stock',
            'price': 'Price',
        }
       