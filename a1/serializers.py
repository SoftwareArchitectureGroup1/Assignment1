from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birthday', 'country', 'description', 'books_count', 'total_sales', 'average_score']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'summary', 'date_of_publication', 'number_of_sales', 'author', 'score']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

class Top10Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'