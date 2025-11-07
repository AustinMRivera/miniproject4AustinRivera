# INF601 - Advanced Programming in Python
# Austin Rivera
# Mini Project 4

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Book
from .forms import BookForm

# Home view - just a welcome page
def home(request):
    return render(request, 'catalog_app/home.html')

# Book list with optional search
# Added a simple search to make it more useful
def book_list(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'catalog_app/book_list.html', {'books': books, 'query': query})

# Detail view for a single book
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'catalog_app/book_detail.html', {'book': book})

# Add book form view
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'catalog_app/add_book.html', {'form': form})

# About page - simple info
def about(request):
    return render(request, 'catalog_app/about.html')

# Register view using Django's UserCreationForm
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'catalog_app/register.html', {'form': form})
