from learn_signals import models
from django.db.models.signals import pre_save,post_save,post_delete
from django.dispatch import receiver
from learn_signals import signals
from django.contrib.auth.models import User


# for Post models 
@receiver(post_save,sender=models.Post)    
def post_check(sender, instance, **kwargs):
    print('post saved')
# post_save.connect(post_save, sender=Post)


def pre_post_save(sender, instance, **kwargs):
    print('pre_post_save done')
pre_save.connect(pre_post_save,sender=models.Post)


# for Profile models 
def create_profile(sender,instance,created,**kwargs):
    if created:
        models.Profile.objects.create(user=instance)
        print('Profile created.')
post_save.connect(create_profile,sender=User)


@receiver(post_save,sender=User)  
def update_profile(sender,instance,created,**kwargs):
    if created == False:
        instance.profile.save()
        print('Profile Updated.')