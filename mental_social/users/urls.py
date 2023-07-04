from django.urls import path
from .views import register , update , ReservationView, get_user
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'reservation', ReservationView, basename='reservation')
urlpatterns = [
    path('register/', register),
    path('update/', update),
    path('getuser/', get_user)


] + router.urls
