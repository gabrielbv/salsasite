from django.conf.urls import patterns, url


from musicmanage import views

urlpatterns = patterns('',

    url(r'^music_manage/$',views.view_music_manage, name='music_manage'),
)
