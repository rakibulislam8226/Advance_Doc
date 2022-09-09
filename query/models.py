from django.db import models
from query.managers import StudentManager,EmployeeManager
# Create your models here.


class Student(models.Model):
    DEPARTMENTS=(
        ('CSE','CSE'),
        ('EEE','EEE'),
    )
    name=models.CharField(max_length=300)
    student_id=models.IntegerField()
    dept=models.CharField(choices=DEPARTMENTS,max_length=5,default='CSE')
    # objects = models.Manager() # The default manager.
    students=models.Manager() #manager changed
    cse_students=StudentManager()
    
    def __str__(self) -> str:
        return f"Student Name: {self.name}" 

class Department(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name
    
    
class Employee(models.Model):
    name=models.CharField(max_length=30)
    age=models.DecimalField(max_digits=4, decimal_places=2)
    dept=models.ForeignKey(Department,on_delete=models.SET_NULL,blank=True, null=True,)
    room_no=models.DecimalField(help_text = "Enter room number.",decimal_places=2,max_digits=5)
    seat_no=models.FloatField(help_text = "Enter seat number.")
    all_employees=EmployeeManager()
    def __str__(self) -> str:
        return f"{self.name} from {self.room_no}"
    
    
    
