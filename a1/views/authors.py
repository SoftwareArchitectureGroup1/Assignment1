from django.shortcuts import render
from django.views import View
from a1.models import Author
from a1.serializers import AuthorSerializer
from rest_framework import filters

class AuthorsTableView(View):
    def get(self, request):
        order_by = request.GET.get('order_by', 'id')
        authors = Author.objects.all().order_by(order_by)

        context = {
            'authors':AuthorSerializer(authors, many=True).data
        }

        return render(request, 'authors.html', context)