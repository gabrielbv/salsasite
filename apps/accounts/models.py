from django.contrib.auth.models import User
from django.db import models

from django_countries import CountryField


# Create your models here.
'''UserProfile is used to create a User profile table with 
the fildes user (takes foreign key ) and country'''

class UserProfile(models.Model):  
	user = models.ForeignKey(User)
	country = CountryField()
