from django.conf.urls import patterns, include, url

#tastypies URL imports
# from django.conf.urls.defaults import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#entry_resource = EntryResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'salsasite.views.home', name='home'),
    # url(r'^salsasite/', include('salsasite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('accounts.urls')),

    url(r'^music/', include('songs.urls')),

    #tastypie URL

#     (r'^blog/', include('myapp.urls')),
#     (r'^api/', include(entry_resource.urls)),
 )
