from gettext import translation
from django.shortcuts import render
from django.http.response import JsonResponse
from .serializers import UserSerializer, doctorSerializer, PersonSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Doctor,Person
from django.contrib.auth.models import User 
from django.db import transaction
# Create your views here.

@api_view(['post'])
def register(request):
    user_type = request.data.get('user_type', None)
    if user_type is None:
        return Response("You must specify a user_type" , status= status.HTTP_400_BAD_REQUEST)
    if user_type =='doctor':
        model_serializer = doctorSerializer(data= request.data)
    elif user_type =='person':
        model_serializer = PersonSerializer(data= request.data)    
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