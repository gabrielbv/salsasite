from django.contrib.auth.models import User
from django.db import models

from django_countries import CountryField


# Create your models here.
class UserProfile(models.Model):
	user = models.ForeignKey(User)
	country = CountryField()