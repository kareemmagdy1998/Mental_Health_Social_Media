from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions
from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer
from .permissions import IsDoctorUser, IsOwnerOrReadOnly, IsCommentOwnerOrReadOnly
from users.serializers import UserSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    # queryset = Comment.objects.filter(parent=None)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs["post_id"]
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs["post_id"]
        post = Post.objects.get(pk=post_id)
        serializer.save(author=self.request.user, post=post)


class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class Posts_List(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class Posts_Pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all() 
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated , IsOwnerOrReadOnly]


class PostsByCreatorList(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        creator_id = self.kwargs['creator_id'] 
        return Post.objects.filter(creator_id=creator_id)


class LikedByListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        try:
            post = Post.objects.get(pk=post_id)
            return post.likes.all()
        except Post.DoesNotExist:
            return []
