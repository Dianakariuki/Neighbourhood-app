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




class Business(models.Model):
  business_name = models.CharField(max_length = 50, null=False)
  profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
  neighbourhood= models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
  business_email = models.EmailField(max_length=100)

  def __str__(self):
    return f'{self.business_name}'

  def create_business(self):
    self.save()

  def delete_business(self):
    Business.objects.filter(id = self.id).delete()

  def find_business(self):
    Business.objects.filter(id =self.id).first()

  def update_business(self):
    """
    A function thta updates the business
   """
  @classmethod
  def filter_by_neighbourhood(cls,id):
    business_gotten = cls.objects.filter(neighbourhood = Neighbourhood.objects.filter(neighbour_id = id).first()).all()
    return business_gotten

  @classmethod
  def search_by_business(cls,search_term):
        business= cls.objects.filter(business_name__icontains=search_term)
        return business