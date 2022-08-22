from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    short_description = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    stock = models.IntegerField(default=20, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name