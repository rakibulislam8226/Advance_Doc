from django.db import models

# Create your models here.
# this model named student for Student model
class School(models.Model):
	name = models.CharField(max_length=255)
    
	def __str__(self):
		return self.name
	

class Student(models.Model):
	name = models.CharField(max_length=255)
	school = models.ForeignKey(School, on_delete=models.SET_NULL,related_name='student', null=True)

	def __str__(self) -> str:
		return f'{self.name}'
