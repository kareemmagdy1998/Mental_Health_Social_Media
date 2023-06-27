from django.urls import path
from .views import register , update


urlpatterns = [
    path('register/', register),
    path('update/', update)

]
