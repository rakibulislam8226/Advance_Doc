from django.shortcuts import render
from django.contrib.auth.models import User
from . import serializers
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer,MessageSerializer,GroupMessageSerializer
from rest_framework import generics


@api_view(['POST'])  
def friend_add(request):
    serializer=serializers.FriendSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])  
def friend_list(request):
    serializer = serializers.FriendSerializers(Friends.objects.all(), many=True)
    return Response(serializer.data)

@api_view(['GET'])  
def block_list(request):
    serializer = serializers.BlockFriendSerializers(BlockFriends.objects.all(), many=True)
    return Response(serializer.data)
    
@api_view(['POST'])  
def add_block(request):
    serializer=serializers.BlockFriendSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)

# Create your views here.
class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]


class MessageDetail(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = "sender"
    
# Create Group views here.
class GroupMessageList(generics.ListCreateAPIView):
    queryset = GroupMessage.objects.all()
    serializer_class = GroupMessageSerializer
    permission_classes = [IsAuthenticated]


class GroupMessageDetail(generics.RetrieveAPIView):
    queryset = GroupMessage.objects.all()
    serializer_class = GroupMessageSerializer
    lookup_field = "sender"
  
