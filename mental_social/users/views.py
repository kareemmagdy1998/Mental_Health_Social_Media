from gettext import translation
from django.shortcuts import render
from django.http.response import JsonResponse
from .serializers import UserSerializer, doctorSerializer, PersonSerializer, ReservationSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Doctor,Person, Reservation
from django.contrib.auth.models import User 
from django.db import transaction
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 

@api_view(['post'])
def register(request):
    user_type = request.data.get('user_type', None)
    if user_type is None:
        return Response("You must specify a user_type" , status= status.HTTP_400_BAD_REQUEST)
    if user_type =='doctor':
        model_serializer = doctorSerializer(data= request.data)
    elif user_type =='person':
        model_serializer = PersonSerializer(data= request.data) 
    else:
        return Response("Invalid user_type specified", status=status.HTTP_400_BAD_REQUEST)       
    user_serializer = UserSerializer(data=request.data)
    if user_serializer.is_valid():
        if model_serializer.is_valid():
            with transaction.atomic():
                user = user_serializer.save()
                model_serializer.save(user=user)
                return Response(model_serializer.data, status=status.HTTP_200_OK)
        errors = model_serializer.errors
    else:
        errors = user_serializer.errors
    return Response(errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['post'])
def update(request):
    print(request.user)
    user = request.user
    doctor = Doctor.objects.filter(user=user).first()
    person = Person.objects.filter(user=user).first()

    if doctor:
        model_serializer_class = doctorSerializer
        model_instance = doctor
    elif person:
        model_serializer_class = PersonSerializer
        model_instance = person

    
    model_serializer = model_serializer_class(instance=model_instance, data=request.data)
    if model_serializer.is_valid():
            model_serializer.save()
            return Response(model_serializer.data, status=status.HTTP_200_OK)
    return Response(model_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservationView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    def create(self, request, *args, **kwargs):
        print(request.user.id)
        person = Person.objects.get(user=request.user)
        request.data['person'] = person.id
        return super().create(request, *args, **kwargs)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    user = User.objects.get(username=request.user.username)
    serializer = UserSerializer(user)
    doctor = Doctor.objects.filter(user=user).first()
    person = Person.objects.filter(user=user).first()
    user_type = ""
    if doctor :
        user_type = "doctor"
    elif person:
        user_type = "person"    

    response_data = {
        'user': serializer.data,
        'user_type': user_type
    }
    return Response(response_data, status=status.HTTP_200_OK)
