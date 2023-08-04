from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.TextField()
    birthday = models.DateTimeField()
    country = models.TextField()
    description = models.TextField()

    @property
    def books_count(self):
        return self.books.count()
    
    @property
    def total_sales(self):
        sales = 0
        for book in self.books.all():
            sales += book.number_of_sales
        return sales