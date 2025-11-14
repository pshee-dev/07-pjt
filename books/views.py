from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Book
from .serializers import CategoryListSerializer, BookListSerializer, BookSerializer
from django.db.models import Count

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookListSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def book_detail(request, book_pk):
    book = Book.objects.annotate(num_of_threads=Count('thread')).get(pk=book_pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)