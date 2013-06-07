from tastypie.resources import ModelResource
from songs.models import Song
from tastypie.authorization import Authorization

from django.contrib.auth.models import User
from tastypie import fields

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'


class SongResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Song.objects.all()
<<<<<<< HEAD
        #resource_name = 'song'
=======
        resource_name = 'song'
>>>>>>> 79c4ff194867cd770ea24ec6ca5cfbb1eb60baa0
