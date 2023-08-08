from django.db import models
from . import Author

class Book(models.Model):
    name = models.TextField()
    summary = models.TextField()
    date_of_publication = models.DateTimeField()
    number_of_sales = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    
    @property
    def score(self):
        reviews = self.reviews.all()
        #reviews = Review.objects.filter(book_id=self.pk)
        if reviews:
            total_rating = sum(review.score for review in reviews)
            return total_rating / len(reviews)
        return 0.0
    