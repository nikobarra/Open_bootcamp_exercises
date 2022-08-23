from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'description', 'stock', 'price')
    list_filter = ('name', 'short_description', 'description', 'stock', 'price')
    search_fields = ('name', 'short_description', 'description', 'stock', 'price')
    ordering = ('name', 'short_description', 'description', 'stock', 'price')
    filter_horizontal = ()
    fieldsets = ()

admin.site.register(Product,ProductAdmin )





