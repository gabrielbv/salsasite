from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
	user = models.ForeignKey(User)
	country = models.CharField()