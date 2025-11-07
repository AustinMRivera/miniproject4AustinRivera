# INF601 - Advanced Programming in Python
# Austin Rivera
# Mini Project 4

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publish_year', 'description']
