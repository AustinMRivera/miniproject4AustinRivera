# INF601 - Advanced Programming in Python
# Austin Rivera
# Mini Project 4

from django.db import models

# Book model with fields for title, author, year, and desc

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publish_year = models.IntegerField()  # Changed to year only for ease
    description = models.TextField()

    def __str__(self):
        return f"{self.title} by {self.author}"
