from django.conf.urls.defaults import *
from songs.api import SongResource, UserResource
from tastypie.api import Api



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

song_resource = SongResource()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(SongResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'salsasite.views.home', name='home'),
    # url(r'^salsasite/', include('salsasite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('accounts.urls')),

    #url(r'^music/', include('songs.urls')),

    url(r'^music/', include('songs.urls')),
    url(r'^api/', include(v1_api.urls)),

 )
