from django.shortcuts import render
from django.http import HttpResponse
from . models import Student, School

# Create your views here.
def home_rlt(request):
  direct = Student.objects.get(school__name = 'Mohakal High Schooll')   # Direct relationship
  # print(f'Student: {direct}')
  
  revierse = School.objects.filter(student__id = 6)  # Reverse relationship
  # print(revierse)
  return HttpResponse('django forward and reverse rlt home.')