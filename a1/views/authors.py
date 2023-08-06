from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from a1.models import Author
from a1.serializers import AuthorSerializer
from a1.forms import AuthorForm
from django.views.generic.edit import CreateView
from django.views.generic import DeleteView
from django.http import JsonResponse

# TODO filtering and ordering
# FIXME missing avg score field
class AuthorsTableView(View):
    def get(self, request):
        order_by = request.GET.get('order_by', 'id')
        authors = Author.objects.all().order_by(order_by)

        context = {
            'authors':AuthorSerializer(authors, many=True).data
        }

        return render(request, 'authors.html', context)

class IndexAuthorsView(View):
    def get(self, request):
        order_by = request.GET.get('order_by', 'id')
        authors = Author.objects.all().order_by(order_by)

        context = {
            'authors': AuthorSerializer(authors, many=True).data
        }

        return render(request, 'indexAuthors.html', context)

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