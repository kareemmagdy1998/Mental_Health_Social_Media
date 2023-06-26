from django.shortcuts import render
from django.http.response import JsonResponse
from .serializers import UserSerializer, doctorSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Doctor,Person

# Create your views here.

@api_view(['post'])
def register(request):
    user_type = request.data.get('user_type')
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        user=serializer.save()
        
        if user_type == 'doctor':
            phone = request.data.get("phone")
            doctor = Doctor(user=user,phone=phone)
            doctor.save()  
        else:
            phone = request.data.get("phone")
            patient = Person(user=user,phone=phone)
            patient.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    