from django.db import models
from django.contrib.auth.models import User

from chat.models import Chat
# Create your models here.
class Friend(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends2')

    def __str__(self):
        return f'{self.user1.username} and {self.user2.username}'

class FriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('sender', 'recipient')
    
    
    
    def accept(self):
        if self.status != 'pending':
            return False
        else:
            
        # Create a new Friend object and save it to the database
            friend = Friend(user1=self.sender, user2=self.recipient)
            print(friend)
            friend.save()
            chat = Chat(participant1=self.sender, participant2=self.recipient)
            chat.save()
            # Update the friend request status to 'accepted'
            self.status = 'accepted'
            self.delete()
            return True
    
    def decline(self):
        if self.status != 'pending':
            return False
        self.delete()