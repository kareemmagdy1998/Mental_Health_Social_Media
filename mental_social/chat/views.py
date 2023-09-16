from django.shortcuts import render
from .serializers import ChatSerializer
from .models import Chat

from django.shortcuts import render 
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view , permission_classes
from django.db.models import Q 
from rest_framework.response import Response
from rest_framework import status

def index(request):
    return render(request, "chat/index.html")
@login_required
def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name,
                                              "username": request.user.username}) 

class ChatView(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_chats(request):
    chats = Chat.objects.filter(Q(participant1=request.user) | Q(participant2=request.user))
    print(chats)
    serializer = ChatSerializer(chats , many=True)
    return Response(serializer.data , status= status.HTTP_200_OK)


def last_30_messages(id):
        chat = Chat.objects.get(id=id)
        return chat.messages.order_by('-timestamp').all()[:30] 
    