from django import forms
from .models import Author  # Replace 'Author' with the name of your model
from .models import Book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birthday', 'country', 'description']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'summary', 'date_of_publication', 'number_of_sales']
        widgets = {
            'date_of_publication': forms.DateInput(attrs={'type': 'date'}),
        }   