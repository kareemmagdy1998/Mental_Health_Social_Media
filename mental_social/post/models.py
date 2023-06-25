from django.db import models
from users.models import Doctor

# Create your models here.

class post(models.Model):
    creator = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)