from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=300)
    def __str__(self) -> str:
        return self.title
 



class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    first_name=models.CharField(max_length=20,null=True,blank=True)
    last_name=models.CharField(max_length=20,null=True,blank=True)
    phone=models.CharField(max_length=15,null=True,blank=True)
    def __str__(self) -> str:
        return str(self.user)
    









