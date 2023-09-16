from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User


    

class Person(models.Model):

    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='person_info' # custom related name
    
    )
    

    
    phone = models.CharField(max_length=50, default="phone")
    birth_date = models.DateField(default=datetime.now)
    gender = models.CharField(max_length=20)
    user_type = models.CharField(default="user", max_length=255)
    profile_picture = models.ImageField(null=True,blank=True)
    

    
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
    
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    



class Doctor(models.Model):
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='doctor' # custom related name
        
    )
    
    profile_picture = models.ImageField(null=True ,blank=True)
    certificate = models.ImageField(upload_to='certificates/', null=True,blank=True)
    specialty = models.CharField(max_length=50)
    office_location = models.CharField(max_length=100, null=True, blank=True,default="office")
    years_of_experience = models.PositiveIntegerField(null=True, blank=True, default=1)
    phone = models.CharField(max_length=50, default="phone")
    birth_date = models.DateField(default=datetime.now)
    gender = models.CharField(max_length=50)
    user_type = models.CharField(default="doctor" , max_length=255)
    about = models.TextField(max_length=250, blank=True)

    
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
    
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
 

class Reservation(models.Model):
        person = models.ForeignKey(Person , related_name='person_reservations' , on_delete=models.CASCADE)
        doctor = models.ForeignKey(Person , related_name='doctor_reservations' , on_delete=models.CASCADE)  
        date = models.DateTimeField()
        class Meta:
            unique_together = ('doctor', 'date')
        def __str__(self):
            return f'{self.person} reserved with {self.doctor} on {self.date}'