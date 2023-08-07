from django.db import models
from . import Book

class Sale(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='sales')
    year = models.IntegerField()
    sales = models.IntegerField()

    def save(self, *args, **kwargs):
        book = self.book
        book.number_of_sales += self.sales
        book.save()
        super(Sale, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        book = self.book
        book.number_of_sales -= self.sales
        book.save()
        super(Sale, self).delete(*args, **kwargs)