from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.TextField()
    birthday = models.DateTimeField()
    country = models.TextField()
    description = models.TextField()