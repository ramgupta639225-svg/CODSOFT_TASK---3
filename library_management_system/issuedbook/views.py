from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import IssuedBook
from .serializers import IssuedBookSerializer


class IssuedBookViewSet(viewsets.ModelViewSet):
    queryset = IssuedBook.objects.all()
    serializer_class = IssuedBookSerializer

