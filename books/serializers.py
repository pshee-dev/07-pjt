from rest_framework import serializers
from .models import Category, Book, Thread, Comment


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'isbn', 'cover')


class BookSerializer(serializers.ModelSerializer):
    
    # 도서의 카테고리 정보(id, name)를 함께 조회 [참조 데이터 조회]
    category = CategoryListSerializer()

    # 도서를 참조하는 게시글 정보(id, title, content, reading_date)를 함께 조회 [역참조 데이터 조회]
    class ThreadSerializer(serializers.ModelSerializer):
        class Meta:
            model = Thread
            fields = ('id', 'title', 'content', 'reading_date')
    
    thread_set = ThreadSerializer(many=True)

    # 도서를 참조하는 게시글 개수 정보를 함께 조회 [역참조 데이터 가공하여 조회]
    num_of_threads = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = '__all__'

    def get_num_of_threads(self, obj):
        return obj.num_of_threads
    

# 게시글의 도서 정보(title)를 함께 조회 [참조 데이터 조회]
class BookTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title',)


class ThreadListSerializer(serializers.ModelSerializer):
    
    book = BookTitleSerializer()

    class Meta:
        model = Thread
        fields = ('id', 'title', 'book')


class CommentDetailSerializer(serializers.ModelSerializer):

    class ThreadTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Thread
            fields = ('title',)

    thread = ThreadTitleSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class ThreadDetailSerializer(serializers.ModelSerializer):
    
    book = BookTitleSerializer(read_only=True)
    comment_set = CommentDetailSerializer(many=True, read_only=True)
    num_of_comments = serializers.SerializerMethodField()
    
    class Meta:
        model = Thread
        fields = '__all__'

    def get_num_of_comments(self, obj):
        return obj.num_of_comments
    

class ThreadCreateSerializer(serializers.ModelSerializer):
    
    book = BookTitleSerializer(read_only=True)

    class Meta:
        model = Thread
        fields = '__all__'