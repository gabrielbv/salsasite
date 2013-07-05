from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie import fields	
from tastypie.authorization import DjangoAuthorization

from songs.models import Song
from accounts.models import User


class UserResource(ModelResource):


    class Meta:

        queryset = User.objects.all()
        resource_name = 'user'
        authorization=Authorization()
            

class SongResource(ModelResource):

    user = fields.ForeignKey(UserResource, 'user', full=True)

    def determine_format(self,request):
        return 'application/json'
    class Meta:
        queryset = Song.objects.filter(status="aproved")
        filtering={
        	"genre":ALL
        }
        authorization=Authorization()  #custom seting for add and edit tastypie-backbone
        always_return_data=True #custom seting for retrieving data in request POST

    def obj_create(self,bundle,**kwargs):
        print("obj_create")
        return super(SongResource,self).obj_create(bundle, user=bundle.request.user)

    def apply_authorization_limits(self,request,object_list):
        return object_list.filter(user=request.user)

