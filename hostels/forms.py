from django import forms
from django.forms.fields import ImageField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'profilePic', 'bio']

class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']