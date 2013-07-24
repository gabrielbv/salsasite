from django.conf.urls import patterns, url

from events import views



urlpatterns = patterns ('',

    
    url(r'^$',views.list,name='event_list'),
    url(r'^add/$',views.add_event,name='add_event'),
    url(r'^(?P<slug>[\w-]+)-(?P<event_id>\d+)/$',views.event_view,name='event_details'),
    url(r'^(?P<slug>[\w-]+)-(?P<event_id>\d+)/edit/$',views.event_edit,name='edit'),
    url(r'^private/$',views.my_events,name='my_events')
    
    )