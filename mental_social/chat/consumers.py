import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .serializers import MessageSerialzer
from django.contrib.auth.models import User
from .views import last_30_messages
from .models import Chat

from .models import Message
class ChatConsumer(WebsocketConsumer):
    def send_chat_message(self, message):    

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message}
        )


    def send_message(self, message):
        self.send(text_data=json.dumps(message))  
          
    def fetch_messages(self, data):
        messages = last_30_messages(data['chatId'])
        serializer = MessageSerialzer(messages, many = True) 
        messages_json = serializer.data
        print(serializer.data)

        content = {
            'command':'messages',
            'messages':messages_json
        }
        self.send_message(content) 

    def new_message(self, data):
        author = data['from']
        chat = Chat.objects.get(id=data['chatId'])
        author_user = User.objects.filter(username=author).first()
        message = Message.objects.create(author = author_user , message = data['message'])
        chat.messages.add(message)
        serializer = MessageSerialzer(message)
        content = {
            'command': 'new_message',
            'message': serializer.data
        }
        return self.send_chat_message(content)

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message
    }


    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        print("Received")
        self.commands[data['command']](self,data)

  

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps(message))

   