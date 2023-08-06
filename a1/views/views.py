from django.shortcuts import render
from a1.models import Author
from a1.serializers import AuthorSerializer

# Create your views here.
def home(request):
    return render(request, 'home.html')

def detailAuthor(request, author_id):
    author = Author.objects.get(pk=author_id)
    context = {
        'author': AuthorSerializer(author, many=False).data
    }
    return render(request, 'detailAuthor.html', context)