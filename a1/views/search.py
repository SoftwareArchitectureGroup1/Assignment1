from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from a1.models import Book
from a1.serializers import BookSerializer

def search(request):
    query = request.GET.get('q')  # Obtener el texto de búsqueda del parámetro 'q' en la URL
    page_number = request.GET.get('page')  # Obtener el número de página del parámetro 'page' en la URL
    book_results = []

    if query:
        for word in query.split():
            # Filtrar los libros cuya descripción contenga alguna de las palabras de búsqueda
            books = Book.objects.filter(summary__icontains=word)
            book_results.extend(list(books))
    else:
        books = Book.objects.all()

    paginator = Paginator(book_results, 10)  # Mostrar 10 libros por página
    page_obj = paginator.get_page(page_number)

    return render(request, 'search.html', {'books':set(book_results), 'page_obj': page_obj, 'query': query})