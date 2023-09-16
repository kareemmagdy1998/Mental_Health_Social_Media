from django.urls import path
from .views import send_friend_request,respond_to_friend_request,list_pending_friend_requests,friends_list,is_friend

urlpatterns = [
    path('send_request/', send_friend_request),
    path('respond_request/', respond_to_friend_request),
    path('list_requests/', list_pending_friend_requests),
    path('list_friends/', friends_list),
    path('is_friend/', is_friend),
]