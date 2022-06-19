from email import message
from locale import currency
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
import neighbour
from neighbour.models import Posts, Profile , Business ,Neighbourhood
from .forms import PostForm, ProfileForm , NeighbourhoodForm , BusinessForm
from django.contrib import messages


@login_required(login_url="/accounts/login/")
def index(request):

  current_user = request.user
  other_neighbours = Profile.objects.filter(neighbourhood_id = request.user.profile.neighbourhood.id).all()
  businesses = Business.objects.filter(neighbourhood_id = request.user.profile.neighbourhood.id).all()
  posts = Posts.objects.filter(neighbourhood_id= request.user.profile.neighbourhood.id).all().order_by('-id')
 

  return render (request , 'neighbour/index.html',{"message":message , "form":upload_neighbourhood ,"myneighbours":other_neighbours, "businesses":businesses ,"posts":posts})

@transaction.atomic
@login_required(login_url ='/accounts/login')
def profile(request):
  current_user = request.user
  user_profile = Profile.objects.filter(id = current_user.id)



  if request.method == 'POST':
    create_profile = ProfileForm(request.POST ,request.FILES ,  instance = request.user.profile )

    if create_profile.is_valid():
      user_profile = create_profile.save(commit = False)
      user_profile.save()

      messages.success(request,('Your profile was successfully updated!'))
      return redirect('profile')
    
    else:
      messages.error(request,"please correct the error below")
  
  else:
     create_profile= ProfileForm(instance= request.user.profile)

    


  return render (request,'neighbour/profile.html', {"form" : create_profile })
