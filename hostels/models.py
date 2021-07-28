from django.db import models

# Create your models here.
class Hostel(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    location=models.CharField(max_length=200)
    image=models.ImageField()
