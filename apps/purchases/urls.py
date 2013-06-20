from django.conf.urls import patterns, url, include



urlpatterns = patterns('',
    

    url(r'^(?P<song_id>\d+)/$' ,'purchases.views.purchase', name='purchase'),
    url(r'^down/$' ,'purchases.views.download', name='down')


)