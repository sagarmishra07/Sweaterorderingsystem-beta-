from django.db import models
from PIL import Image



class Trainning(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.name




class Detail(models.Model):
    id = models.AutoField(primary_key=True)
    size = models.CharField(max_length=100)
    img = models.ImageField(upload_to="static/image", blank=True, null=True)
    colour = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
  

    def __str__(self):
        return self.size


class Feedback(models.Model):
    
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    
  

    def __str__(self):
        return self.name




