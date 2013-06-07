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
        resource_name = 'song'
