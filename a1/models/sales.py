from django.db import models
from . import Book

class Sale(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='sales')
    year = models.IntegerField()
    number_of_sales = models.IntegerField()