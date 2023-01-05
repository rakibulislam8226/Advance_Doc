from django.db import models
from django.contrib.auth.models import User
from django.db import models,transaction
from django.contrib.auth.models import Group

# Create your models here.
class Friends(models.Model):
       user=models.ForeignKey(User,blank=False, null=False, on_delete=models.CASCADE)
       def __str__(self) -> str:
              return str(self.user.username)
       
class BlockFriends(models.Model):
       user=models.ForeignKey(User,related_name='blocked_users', blank=False, null=False,on_delete=models.CASCADE)
       def __str__(self) -> str:
              return str(self.user.username)
       


# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,related_name='receiver')
    message = models.CharField(max_length=1200,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="File's/Images/", blank=True,null=True,max_length=500)
    file=models.FileField(upload_to="File's", blank=True,null=True,max_length=500)

    class Meta:
        ordering = ('-timestamp',)
        
class GroupMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_sender')
    receiver = models.ManyToManyField(User, related_name='group_receiver')
    message = models.CharField(max_length=1200,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="File's/GroupImages/", blank=True,null=True,max_length=500)
    file=models.FileField(upload_to="File's/GroupFile/", blank=True,null=True,max_length=500)
    class Meta:
        ordering = ('-timestamp',)
        
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        if not extra_fields["group_id"]:
            raise ValueError('User must have group id')
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                group = Group.objects.get(extra_fields["group_id"])
                group.user_set.add(user)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password=password, **extra_fields)