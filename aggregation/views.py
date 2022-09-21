
from django.shortcuts import render
from aggregation.models import Book
from django.db.models import Avg, Max, Min, Sum, Count
from django.db.models import Q
from aggregation.models import Publisher
from aggregation.serializers import BookSerializer
from rest_framework import generics
# from .paginator import CustomePagination
from rest_framework import pagination
from rest_framework.pagination import PageNumberPagination
# Create your views here.
# rest api start #
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = PageNumberPagination
    


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# rest api start #
    
    
def book_aggregation(request):
    all_book=Book.objects.all()
    book=Book.objects.aggregate(Avg('price'), Max('price'), Min('price'), Sum('price'))
    rating_total=Book.objects.aggregate(Sum('rating'))
    total_book=Book.objects.count()
    s_book=Book.objects.filter(authors__name='Sohel').count()
    # above_5 = Count('book', filter=Q(book__rating__gt=20))
    # below_5 =Count('book', filter=Q(book__rating__lte=5))
    pub = Publisher.objects.annotate(num_books=Count('book'))
    # above = Publisher.objects.annotate(above_5=above_5)
    # below = Publisher.objects.all().annotate(below_5=below_5)


    context={
        "all_book":all_book,
        "book":book,
        'total_book':total_book,
        'rating_total':rating_total,
        's_book':s_book,
        # 'above_5':above_5,
        # 'below_5':below_5,
        # 'below':below,
        # 'above':above,
        'pub':pub,
        
    }
    return render(request,'book.html',context)