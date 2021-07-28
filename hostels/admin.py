from django.contrib import admin
from .models import Hostels, Profile, Post

# Register your models here.
admin.site.register(Profile)
admin.site.register(Hostels)
admin.site.register(Post)