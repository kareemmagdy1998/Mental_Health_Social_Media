from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Doctor,Person, Reservation


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
    user = UserSerializer(read_only=True)
    class Meta:
        model=Doctor
        fields=["specialty", "office_location", "years_of_experience", "user_type","phone","birth_date","gender","user"]
        # fields="__all__"
    # def create(self, validated_data):
    #             user_data = validated_data.pop('user')
    #             user = User.objects.create_user(**user_data)
    #             doctor = Doctor.objects.create(user=user, **validated_data)
    #             return doctor
     
      
class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Person
        fields=[ "user_type","phone","birth_date","gender","user"]

class ReservationSerializer(serializers.ModelSerializer):
     
     class Meta:
          model = Reservation
          fields = "__all__"