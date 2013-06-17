from django.conf.urls import patterns, url, include
from songs import views


urlpatterns = patterns('',
    

    url(r'^$', 'songs.views.main_index', name='index'),
    #url(r'^create$', 'songs.views.create', name='create'),
    )