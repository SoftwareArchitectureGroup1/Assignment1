from django import template
from django.db.models import Q
from a1.models import Author

register = template.Library()

@register.filter
def filter_authors(authors, filter_params):
    books_count = filter_params.get('books_count')
    average_score = filter_params.get('average_score')
    total_sales = filter_params.get('total_sales')

    filter_kwargs = {}
    if books_count:
        filter_kwargs['books_count'] = books_count
    if average_score:
        filter_kwargs['average_score'] = average_score
    if total_sales:
        filter_kwargs['total_sales'] = total_sales

    print(books_count, average_score, total_sales)
    return authors