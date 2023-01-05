from django.db import models


class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(dept=1)
    def name_queryset(self):
        return super().get_queryset().filter(name='Omor')
    
    
class EmployeeManager(models.Manager):
    def get_age_query(self,age):
        return super().get_queryset().filter(age__gte=age)
    def get_room_then(self,room_no):
        return super().get_queryset().filter(room_no__gte=room_no)
    
    
    
    
    
    
    
    
    
    