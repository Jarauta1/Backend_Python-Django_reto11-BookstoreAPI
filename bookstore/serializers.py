from rest_framework import serializers

from .models import Author, Book
from django.contrib.auth.models import User

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('author_id', 'name', 'added_by', 'created_date')

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('book_id', 'title', 'description', 'author', 'added_by', 'created_date')