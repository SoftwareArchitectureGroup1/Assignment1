from django.db import models
from . import Author

class Book(models.Model):
    name = models.TextField()
    summary = models.TextField()
    date_of_publication = models.DateTimeField()
    number_of_sales = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")