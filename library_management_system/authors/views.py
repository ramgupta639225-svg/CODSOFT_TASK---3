from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from library_management_system.authors.models import Author
from library_management_system.authors.serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer