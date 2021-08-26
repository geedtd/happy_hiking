from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trail(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField(max_length=400)
    length = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
