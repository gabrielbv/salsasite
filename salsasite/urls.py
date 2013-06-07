from django.conf.urls.defaults import *
<<<<<<< HEAD
from songs.api import SongResource
from tastypie.api import Api
#from songs.api.resources import SongResource
=======
from songs.api import SongResource, UserResource
from tastypie.api import Api
<<<<<<< HEAD

>>>>>>> 79c4ff194867cd770ea24ec6ca5cfbb1eb60baa0
=======
from songs.api.resources import MyModelResource
>>>>>>> 559b7e467850fc72e7584bd5ae2ea333782a01e3


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
v1_api = Api(api_name='v1')
v1_api.register(SongResource())

v1_api = Api(api_name='v1')
v1_api.register(MyModelResource())

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

    (r'^api/', include(v1_api.urls))

 )
