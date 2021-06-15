from django.shortcuts import render

from rest_framework import viewsets

from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book

# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('author_id')
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('book_id')
    serializer_class = BookSerializer