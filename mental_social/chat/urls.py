# chat/urls.py
from django.urls import path

from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'chat', views.ChatView, basename='chat')

urlpatterns = [
    path("mychats/", views.get_chats)
] + router.urls