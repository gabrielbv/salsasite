from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie import fields	


from songs.models import Song
from accounts.models import UserProfile


class UserResource(ModelResource):
	class Meta:
	    queryset = UserProfile.objects.all()
        resource_name = 'user'

class SongResource(ModelResource):

    user = fields.ForeignKey(UserResource, 'user')

    def determine_format(self,request):
        return 'application/json'
    class Meta:
        queryset = Song.objects.filter(status="aproved")
        filtering={
        	"genre":ALL
        }
        
        authorization=Authorization()  #custom seting for add and edit tastypie-backbone
        always_return_data=True #custom seting for retrieving data in request POST



