from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Book, Thread
from .serializers import CategoryListSerializer, BookListSerializer, BookSerializer, ThreadListSerializer, ThreadDetailSerializer, ThreadCreateSerializer
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

@api_view(['GET'])
def thread_list(request):
    threads = Thread.objects.all()
    serializer = ThreadListSerializer(threads, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def thread_detail(request, book_pk, thread_pk):
    thread = Thread.objects.annotate(num_of_comments=Count('comment')).get(pk=thread_pk)

    if request.method == 'GET':
        serializer = ThreadDetailSerializer(thread)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ThreadDetailSerializer(thread, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        pk = thread.pk
        thread.delete()
        msg = {
            "message": f'thread {pk} is deleted.'
        }
        return Response(msg, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_thread(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    serializer = ThreadCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(book=book)
        return Response(serializer.data)