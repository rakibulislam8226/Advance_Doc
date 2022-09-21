from urllib import request
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import math
from django.shortcuts import redirect
from django.urls import reverse

## you can override page_size, max_page_size from url query params \

## to make it more dynamic
class CustomePagination(PageNumberPagination):
    page_size = 2
    max_page_size = 1000 
    # last_page_strings ="last"
    page_size_query_param = 'page_size' 
      
    def get_paginated_response(self, data):
        if self.request.query_params.get('page_size'):
            self.page_size = int(self.request.query_params.get('page_size'))
        total_page = math.ceil(self.page.paginator.count / self.page_size)
        return Response({
            'count': self.page.paginator.count,
            'total': total_page,
            'page_size': self.page_size,
            'current': self.page.number,
            'previous': self.get_previous_link(),
            'next': self.get_next_link(),
            'last': self.request.build_absolute_uri('?page=last'),
            # 'last': 'http://127.0.0.1:8000/aggregation/booklist/?page=last',
            'results': data
        })
        

class PersonPagination(PageNumberPagination):
    page_size=2
    page_size_query_param = 'page_size'
    def get_paginated_response(self, data):
        if self.request.query_params.get('page_size'):
            self.page_size = int(self.request.query_params.get('page_size'))

        total_page = math.ceil(self.page.paginator.count / self.page_size)
        return Response({
            'count': self.page.paginator.count,
            'total': total_page,
            'page_size': self.page_size,
            'current': self.page.number,
            'previous': self.get_previous_link(),
            'next': self.get_next_link(),
            'last': self.request.build_absolute_uri('?page=last'),
            # 'last': 'http://127.0.0.1:8000/abstraction/person/?page=last',
            'results': data
        })