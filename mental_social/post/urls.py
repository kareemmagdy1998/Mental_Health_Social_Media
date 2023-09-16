from django.contrib import admin
from django.urls import path, include
from .views import Posts_List,Posts_Pk,CommentListCreateView,CommentRetrieveUpdateDestroyView,PostsByCreatorList

urlpatterns = [
    path('', Posts_List.as_view()),
    path('user/<int:creator_id>', PostsByCreatorList.as_view()),
    path('<int:pk>', Posts_Pk.as_view()),
    path('<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment-retrieve-update-destroy'),
    ]
