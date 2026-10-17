from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter)

    search_fields = ('title', 'author', 'isbn')
    ordering_fields = ('title', 'author', 'isbn')
    sort_fields = ('title', 'author', 'isbn')
