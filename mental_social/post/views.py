from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from .permissions import IsDoctorUser, IsOwnerOrReadOnly

# Create your views here.
class Posts_List(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    print(queryset)
    serializer_class = PostSerializer
    # permission_classes = [IsDoctorUser]


class Posts_Pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsOwnerOrReadOnly]