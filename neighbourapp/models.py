from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ImageField

class Neighbourhood(models.Model):
  neighbourhood_name = models.CharField(max_length=30 , null=False)
  neighbourhood_location = models.CharField(max_length=30, null=False)
  occupants_count = models.IntegerField()
  

  def __str__(self):
    return f'{self.neighbourhood_name}'



  def create_neighbourhood(self):
    """
    A function that saves profile 
    """
    self.save()

  def delete_neighbourhood(self):
    """
    A function that deletes a profile 
    """
    Neighbourhood.objects.filter(id = self.id).delete()

  def find_neighbourhood(self, id):
    """
    A function that gets the neighbourhood by id
    """
    Neighbourhood.objects.filter(id=self.id)



class Profile(models.Model):
  """
  A model that contains user's info for the profile
  """
  name = models.CharField(max_length = 30 , null = False)
  user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',  blank =True)
  bio = models.TextField(max_length=500 , blank =True)
  photo=models.ImageField(upload_to="profile/" , blank=True)
  profile_email=models.EmailField(max_length = 100, blank=True)
  location = models.CharField(max_length=30 , blank=True)
  neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE, blank =True, null=True)

  def __str__(self):
    return f'{self.user.username}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
     if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
     instance.profile.save()



