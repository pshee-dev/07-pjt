from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list),
    path('', views.book_list),
    path('<int:book_pk>/', views.book_detail),
]
