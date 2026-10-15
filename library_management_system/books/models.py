from django.db import models

# Create your models here.

from authors.models import Author


class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    author = models.ForeignKey('authors.Author', on_delete=models.PROTECT, related_name='books')
    category = models.CharField(max_length=100)
    published_date = models.DateField()
    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


