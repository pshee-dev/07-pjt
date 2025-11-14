from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    isbn = models.CharField(max_length=20)
    cover = models.ImageField()
    publisher = models.CharField(max_length=50)
    pub_date = models.DateField()
    author = models.CharField(max_length=50)
    customer_review_rank = models.IntegerField()

class Thread(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    reading_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)