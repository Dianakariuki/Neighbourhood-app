from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

import neighbourapp
from .models import Business, Profile , Neighbourhood , Posts

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']

class NeighbourhoodForm(forms.ModelForm):
  class Meta:
    model = Neighbourhood
    exclude = ['occupants_count']

class PostForm(forms.ModelForm):
  class Meta:
    model = Posts
    exclude= ['profile','neighbourhood']

class BusinessForm(forms.ModelForm):
  class Meta:
    model = Business
    exclude =['profile', 'neighbourhood']
    


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)