from django.conf.urls.defaults import *

from tastypie.api import Api
from django.utils import formats
from songs.api.resources import SongResource
from songs.api.resources import UserResource
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


#urlpatterns += staticfiles_urlpatterns()



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(SongResource())
v1_api.register(UserResource())



urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'salsasite.views.home', name='home'),
    url(r'^news/$', 'salsasite.views.news', name='news'),
    url(r'^gallery/$', 'salsasite.views.gallery', name='gallery'),
    url(r'^uploadedsongs/$', 'salsasite.views.upsongs', name='upsongs'),
 
    

    # url(r'^salsasite/', include('salsasite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('accounts.urls')),
    url(r'^songs/', include('songs.urls')),
    url(r'^purchases/', include ('purchases.urls')),
    #url(r'^news/', include ('salsasite.urls')),

    #(r'^music/', include('songs.urls')),

    (r'^api/', include(v1_api.urls)),

    #(r'^api/', include(v2_api.urls)),


 ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)