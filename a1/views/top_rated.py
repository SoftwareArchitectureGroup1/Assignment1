from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse_lazy
from django.views import View
from a1.models import Book, Review, Sale
from a1.serializers import BookSerializer, ReviewSerializer
from a1.forms import BookForm
from django.views.generic.edit import CreateView
from django.views.generic import DeleteView, DetailView
from django.http import JsonResponse
from operator import attrgetter

class TopRatedTableView(View):
    def get(self, request):
        books = Book.objects.all()
        top_books = sorted(books, key=attrgetter('score'), reverse=True)[:10]
        context = {
            'books': BookSerializer(top_books, many=True).data
        }
        
        
        reviews = {}
        if top_books:
            for book in top_books:
                topReview = Review.objects.filter(book=book).order_by('-number_of_up_votes')[:1]
                worstReview = Review.objects.filter(book=book).order_by('number_of_up_votes')[:1]
                
                topReview_data = ReviewSerializer(topReview, many=True).data
                worstReview_data = ReviewSerializer(worstReview, many=True).data
                
                reviews[book.id] = {
                    'topReview': topReview_data[0]['review'],
                    'worstReview': worstReview_data[0]['review']
                }
                     
            context['reviews'] = reviews
        return render(request, 'topTenBooks.html', context)





