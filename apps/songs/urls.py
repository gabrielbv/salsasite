from django.conf.urls import patterns, url, include
from songs import views


urlpatterns = patterns('',
    

    url(r'^$', 'songs.views.main_index', name='songs'),
    #url(r'^new/$', 'songs.views.add_song', name='new'),
    )