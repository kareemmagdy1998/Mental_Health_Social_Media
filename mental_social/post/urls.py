from django.contrib import admin
from django.urls import path, include
from .views import Posts_List,Posts_Pk
from post.views import CommentListCreateView,CommentRetrieveUpdateDestroyView

urlpatterns = [
    path('', Posts_List.as_view()),
    path('<int:pk>', Posts_Pk.as_view()),
    path('<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment-retrieve-update-destroy'),
    ]
