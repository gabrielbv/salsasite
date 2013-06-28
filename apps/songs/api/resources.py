from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS


from songs.models import Song

class SongResource(ModelResource):

    def determine_format(self,request):
        return 'application/json'
    class Meta:
        queryset = Song.objects.filter(status="aproved")
        filtering={
        	"genre":ALL
        }
        
        authorization=Authorization()  #custom seting for add and edit tastypie-backbone
        always_return_data=True #custom seting for retrieving data in request POST



