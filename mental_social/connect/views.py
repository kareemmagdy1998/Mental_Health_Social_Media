from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import FriendRequest,Friend
from .serializers import FriendRequestSerializer,FriendSerializer
from rest_framework.permissions import IsAuthenticated
from .utils import get_friends
from django.http import JsonResponse
from users.serializers import UserSerializer
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_friend_request(request):
    recipient_id = request.data.get('recipient_id')

    if not recipient_id:
        return Response({'error': 'recipient_id is required'}, status=status.HTTP_400_BAD_REQUEST)

    sender = request.user
    recipient = User.objects.filter(id=recipient_id).first()

    # check if recipient exists
    if not recipient or sender==recipient:
        return Response({'error': 'Invalid recipient_id'}, status=status.HTTP_400_BAD_REQUEST)

    # check if there is already a friend request between the two users
    if FriendRequest.objects.filter(sender=sender, recipient=recipient).exists():
        return Response({'error': 'Friend request already exists'}, status=status.HTTP_400_BAD_REQUEST)

    # create a new friend request
    friend_request = FriendRequest(sender=sender, recipient=recipient)
    friend_request.save()

    serializer = FriendRequestSerializer(friend_request)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def respond_to_friend_request(request):
    friend_request_id = request.data.get('friend_request_id')
    response = request.data.get('response')

    if not friend_request_id or not response:
        return Response({'error': 'friend_request_id and response are required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        friend_request = FriendRequest.objects.get(id=friend_request_id)
    except FriendRequest.DoesNotExist:
        return Response({'error': 'Invalid friend_request_id'}, status=status.HTTP_400_BAD_REQUEST)

    if friend_request.recipient != request.user:
        return Response({'error': 'You do not have permission to respond to this friend request'}, status=status.HTTP_403_FORBIDDEN)

    if response == 'accept':
       if friend_request.accept():
            serializer = FriendRequestSerializer(friend_request)
            return Response(serializer.data,status.HTTP_200_OK,status)
       return Response("friend_request already had been accepted", status.HTTP_403_FORBIDDEN)

    elif response == 'decline':
        if friend_request.decline():
            return Response("friend_request declined", status.HTTP_202_ACCEPTED)
        return Response("friend_request already had been accepted", status.HTTP_403_FORBIDDEN)
    else:
        return Response({'error': 'Invalid response'}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_pending_friend_requests(request):
    user = request.user

    friend_requests = FriendRequest.objects.filter(recipient=user, status='pending')
    serializer = FriendRequestSerializer(friend_requests, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def friends_list(request):
    user = request.user
    friends1 = Friend.objects.filter(user1=user).exclude(user2=user)
    friends2 = Friend.objects.filter(user2=user).exclude(user1=user)
    friends = friends1 | friends2
    serializer = FriendSerializer(friends, many=True)
    return Response(serializer.data)