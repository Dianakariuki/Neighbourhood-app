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

def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search_by_business(search_term)
        message = f"{search_term}"

        return render(request, 'neighbour/search.html',{"message":message,"business": searched_business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'neighbour/search.html',{"message":message})

def post(request):
  current_user = request.user

  if request.method == 'POST':
    upload_post = PostForm(request.POST, request.FILES)

    if upload_post.is_valid():
      post = upload_post.save(commit=False)
      post.profile = current_user.profile
      post.neighbourhood = current_user.profile.neighbourhood
      post.save()

      return redirect('index')
  else :
      upload_post = PostForm()

  return render(request ,'neighbour/post.html', {"form":upload_post})
