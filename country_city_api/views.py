from django.shortcuts import render

# Create your views here.
from . models import *
from . serializers import *
from rest_framework import generics,viewsets
from rest_framework import filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView, Response


# Create your views here.
class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^name',]
    filter_backends=(SearchFilter,OrderingFilter)
    
class CountryDetailsView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailsSerializer
    lookup_field = "name"
    

class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^name']
    filter_backends=(SearchFilter,OrderingFilter)

class CitySearchView(APIView):
    def get(self, request, country=None, format=None):
        city = request.GET.get('q', None)
        if city is not None:
            cities = City.objects\
            .filter(name__icontains=city) \
            .filter(country__name=country)
            res_data = CitySerializer(cities, many=True).data
            return Response(res_data)
        return Response([])
    
class CityDetailsView(APIView):
    def get(self, request, country=None, city=None, format=None):
        if city is not None:
            cities = City.objects\
            .filter(name=city) \
            .filter(country__name=country).first()
            res_data = CitySerializer(cities).data
            return Response(res_data)
        return Response({})