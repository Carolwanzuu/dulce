from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profilePic=models.ImageField(blank=True,null=True,upload_to = 'images/', default='default.png')
    bio=models.TextField(max_length=255,blank=True)
    name=models.CharField(max_length=50,blank=True)
    contact=models.EmailField(max_length=100, blank=True)

class Hostels(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    location=models.CharField(max_length=200)
    image=models.ImageField()

class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    hood = models.ForeignKey(Hostels, on_delete=models.CASCADE, related_name='hood_post')