from tastypie.resources import ModelResource
from songs.models import Song


class SongResource(ModelResource):
    class Meta:
        queryset = Song.objects.all()
        resource_name = 'Song'