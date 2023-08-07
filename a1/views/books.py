from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse_lazy
from django.views import View
from a1.models import Book, Author
from a1.serializers import BookSerializer
from a1.forms import BookForm
from django.views.generic.edit import CreateView
from django.views.generic import DeleteView, DetailView
from django.http import JsonResponse

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'create_book.html'
    success_url = reverse_lazy('indexAuthor')

    def form_valid(self, form):
        author = Author.objects.get(pk=self.kwargs['author_id'])
        
        book = form.save(commit=False)
        book.author = author
        book.save()
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        initial['number_of_sales'] = 0
        return initial
    
    

class BookDetailView(DetailView):
    model = Book
    template_name = 'detail_book.html'
    context_object_name = 'books'

class EditBookView(View):
    template_name = 'edit_book.html'
    form_class = BookForm

    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        form = self.form_class(instance=book)
        return render(request, self.template_name, {'form': form, 'book': book})

    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        form = self.form_class(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('detail-book', pk=book_id)
        return render(request, self.template_name, {'form': form, 'book': book})

def delete_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        print(book)
        print("xd")
        book.delete()
        return JsonResponse({'message': 'Book deleted successfully.'})
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': 'Error deleting book.'}, status=500)



