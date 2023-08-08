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
    def average_score(self):
        all_books = self.books.all()
        counter = 0
        total = 0
        if all_books:
            for book in all_books:
                reviews = book.reviews.all()
                if reviews:
                    for review in reviews:
                        counter+=1
                        total+= review.score
                    return float(f'{total/counter:.2f}')
                else:
                    return 0
        else:
            return 0

    @property
    def total_sales(self):
        sales = 0
        for book in self.books.all():
            sales += book.number_of_sales
        return sales
