from django.contrib import admin
from .models import Author, Book, Review, Sale

class BookInline(admin.StackedInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Review)
admin.site.register(Sale)