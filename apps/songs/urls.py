from django.conf.urls import patterns, url, include
from songs import views
from tastypie.api import Api
from songs.api import SongResource, UserResource


v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(SongResource())

urlpatterns = patterns('',
    
    url(r'^$', 'songs.views.index', name='index'),
    url(r'^create$', 'songs.views.create', name='create'),
    url(r'^api/', "include(v1_api.urls)"),
    url(r'^backbone$', 'songs.views.backbone', name='backbone'),