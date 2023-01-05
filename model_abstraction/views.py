from django.shortcuts import render
from model_abstraction.serializers import (
    AbsBookSerializer,
    PersonSerializer,
    StudentDIUSerializer, 
    StudentGUBSerializer,
    ISBNSerializer,
    )
from rest_framework import generics
from model_abstraction import models
# from aggregation.paginator import CustomePagination
from rest_framework.pagination import PageNumberPagination
# Create your views here.

# StudentGUB api start #
class StudentGUBList(generics.ListCreateAPIView):
    queryset = models.StudentGUB.objects.all()
    serializer_class = StudentGUBSerializer
    pagination_class = PageNumberPagination


class StudentGUBDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StudentGUB.objects.all()
    serializer_class = StudentGUBSerializer
# StudentGUB api start #


# StudentDIU api start #
class StudentDIUList(generics.ListCreateAPIView):
    queryset = models.StudentDIU.objects.all()
    serializer_class = StudentDIUSerializer


class StudentDIUDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StudentDIU.objects.all()
    serializer_class = StudentDIUSerializer
# StudentDIU api start #


# Book api start #
class AbsBookList(generics.ListCreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = AbsBookSerializer


class AbsBookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Book.objects.all()
    serializer_class = AbsBookSerializer
# Book api end #


# ISBN api start #
class ISBNList(generics.ListCreateAPIView):
    queryset = models.ISBN.objects.all()
    serializer_class = ISBNSerializer


class ISBNDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ISBN.objects.all()
    serializer_class = ISBNSerializer
# ISBN api end #

# Person api start #
class PersonList(generics.ListCreateAPIView):
    queryset = models.Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = PageNumberPagination


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Person.objects.all()
    serializer_class = PersonSerializer
# Person api end #