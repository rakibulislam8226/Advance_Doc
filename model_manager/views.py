
from django.shortcuts import render
from . models import Employee, Student
# Create your views here.

def StudentView(request):
    student=Student.cse_students.get_queryset()
    return render(request,'students.html',{"student":student})

def EmploeeView(request):
    employee=Employee.all_employees.get_room_then(300) and Employee.all_employees.get_age_query(10)
    # employee=Employee.all_employees.get_age_query(21)
    return render(request,'employee.html',{"employee":employee})