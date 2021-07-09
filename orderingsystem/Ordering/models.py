from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.

class Ordering(models.Model):
    id = models.AutoField(primary_key=True)
    
    username = models.CharField(max_length=25, default=0)
    size = models.CharField(max_length=50)
    
    colour = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    Total = models.IntegerField(default=0)
    
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=15)
    location = models.CharField(max_length=50)
    ordered_date = models.DateField(auto_now=True, blank=False)
   
    delivered_date =  models.CharField(max_length=50)
    
    delivered = models.CharField(max_length=50, default="NotDelivered")
    verified = models.CharField(max_length=50, default="NotReceived")
    
    
    def __str__(self):
        return self.username



