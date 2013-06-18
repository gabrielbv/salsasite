from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from songs.models import Song

class SongResource(ModelResource):

    def determine_format(self,request):
        return 'application/json'
    class Meta:
        queryset = Song.objects.all()
        
        authorization=Authorization()
        always_return_data=True



