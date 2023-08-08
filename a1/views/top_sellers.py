from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse_lazy
from django.views import View
from a1.models import Book, Review, Sale, Author
from a1.serializers import BookSerializer, ReviewSerializer, AuthorSerializer
from a1.forms import BookForm
from django.views.generic.edit import CreateView
from django.views.generic import DeleteView, DetailView
from django.http import JsonResponse
from operator import attrgetter

def idExistOnIndex(my_list, target_element):
    for sub_list in my_list:
        if len(sub_list) > 0 and sub_list[0] == target_element:
            return True
    return False


class TopSellerTableView(View):
    def get(self, request):
        top_books = Book.objects.all().order_by('-number_of_sales')[:50]

        
        salesPerYear = []
        topSales = {}
        authors = {}
        context = {
            'books': BookSerializer(top_books, many=True).data
        }
                
        if top_books:
            for book in top_books:
                salesPublicationYear = Sale.objects.filter(year=book.date_of_publication.year)
                if salesPublicationYear:
                    sales = 0
                    for sale in salesPublicationYear:
                        for value in salesPublicationYear:
                            if sale.book.id == value.id:
                                sales += sale.sales
                        salesPerYear.append([sale.book.id, sales])
                        
                    salesPerYear.sort(key = lambda x: x[1], reverse=True)
                    salesPerYear = salesPerYear[:5]
                    if idExistOnIndex(salesPerYear, book.id):
                        topSales[book.id] = {
                            'bestseller': "Best Seller"
                        }
                    else:
                        topSales[book.id] = {
                                'bestseller': "No"
                        }
                    salesPerYear = []
                    context['topSales'] = topSales
                    
                author = Author.objects.get(id=book.author.id) 
                author_data = AuthorSerializer(author).data
                authors[book.id] = {
                    'total_sales': author_data['total_sales']
                }
                context['total_sales'] = authors               
        return render(request, 'topFiftyBooks.html', context)





