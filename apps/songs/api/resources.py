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

    class Meta:
        queryset = Song.objects.filter(status="aproved").order_by('artist')
        filtering={
        	"genre":ALL,
            "status": ALL,
        }
        #authentication = BasicAuthentication()
        authorization=Authorization()  #custom seting for add and edit tastypie-backbone
        always_return_data=True #custom seting for retrieving data in request POST

    def determine_format(self,request):
        return 'application/json'

    def obj_create(self,bundle,**kwargs):
        print("obj_create", request.user)
        return super(SongResource,self).obj_create(bundle, user=bundle.request.user)


class UserSongsResource(SongResource):
    
    class Meta:
        filtering={
            "genre":ALL,
            "status": ALL,
        }
        queryset=Song.objects.all()
    def get_object_list(self, request):
        print("hi there")
        return super(UserSongsResource, self).get_object_list(request).filter(user=request.user)
    
