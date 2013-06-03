from django.conf.urls import patterns, url


from songs import views

urlpatterns = patterns('',

    url(r'^add/$',views.add_song, name='add_song'),
)
