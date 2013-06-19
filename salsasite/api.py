from tastypie.resources import ModelResource
from songs.models import Song
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from myapp.models import Entry


class SongResource(ModelResource):
    class Meta:
        queryset = Song.objects.all()
        resource_name = 'song'