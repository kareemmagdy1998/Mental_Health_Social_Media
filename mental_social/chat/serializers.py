from rest_framework import serializers 
from .models import Message , Chat
from users.serializers import UserSerializer
class MessageSerialzer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Message
        fields = ['author' , 'message' , 'timestamp'] 

class ChatSerializer(serializers.ModelSerializer):
    messages = MessageSerialzer(many=True)
    participant1 = UserSerializer()
    participant2 = UserSerializer() 
    class Meta:
        model = Chat
        fields ='__all__'   