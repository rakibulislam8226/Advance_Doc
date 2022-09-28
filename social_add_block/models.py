from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Friends(models.Model):
       user=models.ForeignKey(User,blank=False, null=False, on_delete=models.CASCADE)
       def __str__(self) -> str:
              return str(self.user.username)
       
class BlockFriends(models.Model):
       user=models.ForeignKey(User,related_name='blocked_users', blank=False, null=False,on_delete=models.CASCADE)
       def __str__(self) -> str:
              return str(self.user.username)