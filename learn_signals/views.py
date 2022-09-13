from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from model_abstraction import models
from learn_signals import serializers,models
from django.db.models.signals import pre_save,post_save,post_delete
from django.dispatch import receiver,Signal
# Create your views here.


# Post api start #
class PostList(generics.ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
# Post api start #

# your_post_created=Signal(providing_args=['please'])
# signal_home=Signal()


# def signals_home(request):
#     # signal_home.send(sender=models.Post,)
#     signal_home.send(sender=models.Post)
#     return HttpResponse("home for signals.")
    
# @receiver(signal_home,sender=models.Post)    
# def post_check(sender, instance, **kwargs):
#     print('post views saved')