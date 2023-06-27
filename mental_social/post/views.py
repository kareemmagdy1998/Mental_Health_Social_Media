from django.shortcuts import render,get_object_or_404
from rest_framework import generics, permissions
from .models import Comment ,Post
from .serializers import CommentSerializer


class CommentListCreateView(generics.ListCreateAPIView):
    # queryset = Comment.objects.filter(parent=None)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        post = Post.objects.get(pk=post_id)
        serializer.save(author=self.request.user, post=post)

class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer    



