from rest_framework import serializers
from .models import Friends,BlockFriends


        
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

