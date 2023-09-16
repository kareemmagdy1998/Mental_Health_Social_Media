from django.contrib.auth import get_user_model
from .models import Friend

def get_friends(user):
    # Retrieve all Friend objects that involve the user
    friends1 = Friend.objects.filter(user1=user)
    friends2 = Friend.objects.filter(user2=user)

    # Combine the other user in each friendship and return as a list
    friends = []
    for friend in friends1:
        friends.append(friend.user2.username)
    for friend in friends2:
        friends.append(friend.user1.username)

    return friends