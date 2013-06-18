from tastypie.resources import ModelResource
from songs.models import Song
from tastypie.authorization import Authorization

from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authorization import Authorization

from myapp.models import Entry


class EntryResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'


class SongResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Song.objects.all()
        resource_name = 'song'
