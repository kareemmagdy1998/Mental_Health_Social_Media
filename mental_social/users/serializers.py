from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Doctor,Person

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
        extra_kwargs = {
            'password':{'write_only': True},
        }
        
    def create(self, validation_data):
            password = validation_data.pop('password', None) 
            instance = self.Meta.model(**validation_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance
        

    def update(self, instance, validated_data):
            password = validated_data.pop('password', None)
            instance = super().update(instance, validated_data)
            if password is not None:
                instance.set_password(password)
                instance.save()
            
            return instance
    
    

class doctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields="__all__"
     
      
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields="__all__"            