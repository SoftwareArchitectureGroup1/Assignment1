from django import forms
from .models import Author  # Replace 'Author' with the name of your model

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birthday', 'country', 'description']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }