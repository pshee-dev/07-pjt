from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list),
    path('', views.book_list),
    path('<int:book_pk>/', views.book_detail),
    path('threads/', views.thread_list),
    path('<int:book_pk>/threads/<int:thread_pk>/', views.thread_detail),
    path('<int:book_pk>/threads/create/', views.create_thread),
    path('<int:book_pk>/threads/<int:thread_pk>/comments/create/', views.create_comment),
    path('<int:book_pk>/threads/<int:thread_pk>/comments/<int:comment_pk>/', views.comment_detail),
]
