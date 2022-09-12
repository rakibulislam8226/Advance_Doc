from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    def __str__(self) -> str:
        return self.name 

class Publisher(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self) -> str:
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author,related_name='author')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()
    def authorall(self):
        return ", ".join([str(p) for p in self.authors.all()])
    
    def __str__(self) -> str:
        return f"Book Name: {self.name}, Aurthor: {self.authors}"

class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    def __str__(self) -> str:
        return self.name
    
    
    
    
    