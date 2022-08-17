from django.db import models
from datetime import date

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name


class Entry(models.Model):
    author = models.foreignKey(Author, on_delete=models.CASCADE)
    headline=models.CharField(max_length=255)
    body_text=models.TextField()
    public_date=models.DateField(default = date.today)
    rating = models.IntegerField(default = 5)
    
    def __str__(self):
        return self.headline

