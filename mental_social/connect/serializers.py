from rest_framework import serializers
from connect.models import FriendRequest,Friend
from users.serializers import UserSerializer
from django.contrib.auth.models import User

class FriendRequestSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    recipient = UserSerializer(read_only=True)

    class Meta:
        model = FriendRequest
        fields = ['id', 'sender', 'recipient', 'status', 'created_at']
        

class FriendSerializer(serializers.ModelSerializer):
    
    user1 = UserSerializer()
    user2 = UserSerializer()
    
    class Meta:
        model = Friend
        fields = ['user1', 'user2']
