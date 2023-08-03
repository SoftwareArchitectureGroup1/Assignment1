from django.db import models

class Sale(models.Model):
    name = models.TextField()
    year = models.IntegerField()
    number_of_sales = models.IntegerField()