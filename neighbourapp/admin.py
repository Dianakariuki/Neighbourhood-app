from django.contrib import admin
from .models import Neighbourhood, Profile ,Business

# Register your models here.
admin.site.register(Business)
admin.site.register(Profile)
admin.site.register(Neighbourhood)
