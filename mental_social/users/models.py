from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator


class Person(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    
    person = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='person_info', # custom related name
        default=1
    )
    
    phone = models.CharField(max_length=50, default="phone")
    birth_date = models.DateField(default=datetime.now)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES , default=MALE)

    
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
    
    
    def __str__(self):
        return f'{self.person.first_name} {self.person.last_name}'


class Doctor(models.Model):
    
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    
    SPECIALTY_CHOICES = [
        ('Dermatologist', 'Dermatologist'),
        ('Cardiologist', 'Cardiologist'),
        ('Pediatrician', 'Pediatrician'),
        ('Ophthalmologist', 'Ophthalmologist'),
        ('Neurologist', 'Neurologist'),
    ]
    
    person = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='doctor', # custom related name
        default=1
    )
 
    certificate = models.ImageField(upload_to='certificates/')
    specialty = models.CharField(max_length=50, choices=SPECIALTY_CHOICES , default='Dermatologist')
    office_location = models.CharField(max_length=100, null=True, blank=True,default="office")
    years_of_experience = models.PositiveIntegerField(null=True, blank=True, default=1)
    phone = models.CharField(max_length=50, default="phone")
    birth_date = models.DateField(default=datetime.now)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES , default=MALE)

    
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
    
    
    def __str__(self):
        return f'{self.person.first_name} {self.person.last_name}'
    
    