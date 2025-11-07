# INF601 - Advanced Programming in Python
# Austin Rivera
# Mini Project 4

from django.contrib import admin
from .models import Book

# Customizing the admin interface for the Book model
# I added some filters and search to make it easier to use
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_year')  # Changed field name for variety
    search_fields = ('title', 'author')
    list_filter = ('publish_year',)
    ordering = ('title',)

admin.site.register(Book, BookAdmin)
