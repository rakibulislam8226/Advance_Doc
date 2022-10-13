from rest_framework import serializers
from .models import Friends,BlockFriends,Message,GroupMessage
from django.contrib.auth.models import User

        
class FriendSerializers(serializers.ModelSerializer):
    def getUsername(self, obj):
        return obj.user.username
    friend_name = serializers.SerializerMethodField("getUsername")
    class Meta:
        model = Friends
        fields = ('id', 'user','friend_name')
    
    def validate(self, data):
        friend_exist = Friends.objects.filter(user=data['user']).first()
        block_exist = BlockFriends.objects.filter(user=data['user']).first()
        if block_exist:
            raise serializers.ValidationError("You Can't Add friend to a blocked person.")
        if friend_exist:
            raise serializers.ValidationError('Friend already present in your friend list')
        return data

        
class BlockFriendSerializers(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    class Meta:
        model = BlockFriends
        fields = ('id', 'user','username')
    
    def validate(self, data):
        friend_exist = Friends.objects.filter(user=data['user']).first()
        block_exist = BlockFriends.objects.filter(user=data['user']).first()
        if block_exist:
            raise serializers.ValidationError("This person is already blocked.")
        if friend_exist:
            friend_exist.delete()
        return data

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']
        
class ReceiverUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username',]
        

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message','image', 'file','timestamp',]     
           
    def create(self, validated_data):
        sender = self.context['request'].user
        entity = Message.objects.create(sender=sender, **validated_data)
        return entity

# Group Message
class GroupMessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = ReceiverUserSerializer(read_only=True, many=True)

    class Meta:
        model = GroupMessage
        fields = ['sender', 'receiver', 'message','image', 'file','timestamp',]     
           
    def create(self, validated_data):
        sender = self.context['request'].user
        entity = GroupMessage.objects.create(sender=sender, **validated_data) 
        return entity
    
 