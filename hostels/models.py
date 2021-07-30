from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES=(
    ('All','All'),
    ('Male','Male'),
    ('Female','Female')
)
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
    image=models.ImageField(blank=True)
    gender=models.CharField(max_length=100, choices=GENDER_CHOICES, blank=True)
    price=models.IntegerField(null=True)
    requirements=models.TextField(blank=True)
    rooms=models.CharField(max_length=100, blank=True)
    amenities=models.CharField(max_length=200, null=True)

class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    

class HostelNewsRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()