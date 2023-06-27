from django.contrib import admin
from django.urls import path, include
from .views import Posts_List,Posts_Pk

urlpatterns = [
    path('', Posts_List.as_view()),
    path('<int:pk>', Posts_Pk.as_view())
]
