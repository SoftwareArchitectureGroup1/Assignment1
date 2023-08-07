from django import forms
from .models import Author
from .models import Sale
from .models import Book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birthday', 'country', 'description']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }

class SaleForm(forms.ModelForm):
    YEAR_CHOICES = [(year, year) for year in range(2000, 2031)]
    year = forms.ChoiceField(choices=YEAR_CHOICES, widget=forms.Select)
    class Meta:
        model = Sale
        fields = ['year', 'number_of_sales']

