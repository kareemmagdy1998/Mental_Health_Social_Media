from django.contrib import admin
from django.urls import path, include

from post.views import CommentListCreateView,CommentRetrieveUpdateDestroyView

urlpatterns = [
    path('<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment-retrieve-update-destroy'),
    ]
