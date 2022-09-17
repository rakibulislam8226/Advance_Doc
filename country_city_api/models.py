from django.db import models

# Create your models here.

class Country(models.Model):
       name = models.CharField(max_length=100, null=False, blank=False, unique= True)

       def __str__(self) -> str:
              return self.name

class City(models.Model):
       name = models.CharField(max_length=100)
       country = models.ForeignKey(Country,on_delete=models.CASCADE, null=False, blank=False, related_name='cities')

       def __str__(self) -> str:
              return self.name