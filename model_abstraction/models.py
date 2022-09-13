from django.utils import timezone
from django.db import models

# Create your models here.
########## Abstract base classes #
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    
    class Meta:
        abstract = True
        ordering=['age']

class StudentGUB(CommonInfo):
    home_group = models.CharField(max_length=50)
    
    class Meta(CommonInfo.Meta):
        ordering=['name']
    
class StudentDIU(CommonInfo):
    studentid = models.PositiveIntegerField()
    
########## Abstract base classes end #
    
    
######### Multi-table inheritance Start # make one to one relation create
class Book(models.Model):
    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    
class ISBN(Book):
    ISBN=models.TextField()
    
 ######### Multi-table inheritance end #   
    
    
######### Proxy models start #   provide different interface
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30) 
    created = models.DateTimeField(auto_now_add=True)
    
class MyPerson(Person): # auto create one when create a another
    class Meta:
        proxy = True
        ordering=['first_name']
        
    def created_on(self):
        return timezone.now() - self.created
    
######### Proxy models end #   
    
    
    
    
    
    
    