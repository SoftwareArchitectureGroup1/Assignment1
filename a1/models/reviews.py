from django.db import models
from . import Book

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    score = models.IntegerField()
    number_of_up_votes = models.IntegerField(default=0)
    number_of_down_votes = models.IntegerField(default=0)