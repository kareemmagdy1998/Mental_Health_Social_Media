from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.message}'
    
    

class Chat(models.Model):
    participant1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat')
    participant2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats')
    messages = models.ManyToManyField(Message , blank=True)


    def __str__(self):
        return "{}".format(self.pk)