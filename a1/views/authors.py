from django.db.models.functions import Cast
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from a1.models import Author
from django.db.models import F, FloatField
from a1.models import Book
from a1.serializers import AuthorSerializer
from a1.forms import AuthorForm
from django.views.generic.edit import CreateView
from django.views.generic import DeleteView
from django.http import JsonResponse
from django.views.generic import DetailView
from operator import attrgetter

# TODO filtering and ordering
# FIXME missing avg score field
class AuthorsTableView(View):
    def get(self, request):
        order_by = request.GET.get('order_by', 'id')
        print(order_by)
        authors = Author.objects.all().order_by(order_by)

        context = {
            'authors':AuthorSerializer(authors, many=True).data
        }

        return render(request, 'authors.html', context)

class IndexAuthorsView(View):
    def get(self, request):
        sort_by = request.GET.get('sort_by', 'id')
        sort_order = request.GET.get('sort_order', 'asc')  # Default sort order ascending
        special_fields = ['books_count', 'average_score',
                             'total_sales']
        if sort_by not in special_fields:
            authors = Author.objects.all().order_by(sort_by)
        else:
            authors = Author.objects.all()
            if (sort_order == "asc"):
                reverse = False
            else:
                reverse = True
            sorted_authors = sorted(authors, key=attrgetter(sort_by), reverse=reverse)
            authors = sorted_authors
        context = {
            'authors': AuthorSerializer(authors, many=True).data,
            'sort_order': sort_order,
        }
        return render(request, 'indexAuthors.html', context)

    def post(self, request):
        try:
            author = Author.objects.get(id=request.POST.get("author_id"))
            author.delete()
            return JsonResponse({'message': 'Author deleted successfully.'})
        except Author.DoesNotExist:
            return JsonResponse({'error': 'Author not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 'Error deleting author.'}, status=500)

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'createAuthor.html'
    success_url = reverse_lazy('indexAuthor')
    
def delete_author(request, author_id):
    try:
        author = Author.objects.get(id=author_id)
        author.delete()
        return JsonResponse({'message': 'Author deleted successfully.'})
    except Author.DoesNotExist:
        return JsonResponse({'error': 'Author not found.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': 'Error deleting author.'}, status=500)

class EditAuthorView(View):
    template_name = 'edit-author.html'
    form_class = AuthorForm

    def get(self, request, author_id):
        author = get_object_or_404(Author, id=author_id)
        form = self.form_class(instance=author)
        return render(request, self.template_name, {'form': form, 'author': author})

    def post(self, request, author_id):
        author = get_object_or_404(Author, id=author_id)
        form = self.form_class(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('indexAuthor')
        return render(request, self.template_name, {'form': form, 'author': author})

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'detailAuthor.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.get_object()
        books = author.books.all()
        context['books'] = books
        return context