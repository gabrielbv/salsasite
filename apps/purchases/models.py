from django.db import models
from songs.models import Song
from django.contrib.auth.models import User


# Create your models here.

class Purchase(models.Model):

    user = models.ForeignKey(User)
    song = models.ForeignKey(Song)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

