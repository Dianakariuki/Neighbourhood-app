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


