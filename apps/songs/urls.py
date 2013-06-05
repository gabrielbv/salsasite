from django.conf.urls import patterns, url


from songs import views

urlpatterns = patterns('',

    url(r'^add/$',views.add_song, name='add_song'),
    url(r'^add_song_confirm/$',views.add_song_confirm, name='add_song_confirm'),
<<<<<<< HEAD
    url(r'^(?P<song_id>\d+)/$',views.song_view, name='song_view'),
    url(r'^index/$', views.index, name='index'),
    # ex: /polls/5/
    #url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
=======
    url(r'^(?P<song_id>\d+)/edit/$',views.song_edit, name='song_edit'),
>>>>>>> 6f3cee930569873dc41cb911ea2f424e3dbc1eac
)

