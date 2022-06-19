from email import message
from locale import currency
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
import neighbour
from neighbour.models import Posts, Profile , Business ,Neighbourhood
from .forms import PostForm, ProfileForm , NeighbourhoodForm , BusinessForm
from django.contrib import messages
