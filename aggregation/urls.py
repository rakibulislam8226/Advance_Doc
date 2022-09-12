from django.urls import path
from . views import *
urlpatterns = [
    path('book/',book_aggregation, name='book'),
    path('booklist/', BookList.as_view()),
    path('booklist/<int:pk>/', BookDetail.as_view()),
]
