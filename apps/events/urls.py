from django.conf.urls import patterns, url

from events import views



urlpatterns = patterns ('',


    
    url(r'^list/$',views.list,name='event_list'),
    url(r'^add/$',views.change,name='add_event'),
    url(r'^(?P<slug>[\w-]+)-(?P<event_id>\d+)/$',views.event_view,name='event_details'),
    url(r'^(?P<slug>[\w-]+)-(?P<event_id>\d+)/edit/$',views.change,name='edit'),
    url(r'^private/$',views.my_events,name='my_events'),
    url(r'^$',views.backbone,name='backbone'),
   


    # url(r'^$',views.generic_list,name='events_list'),
    # url(r'^private/$',views.generic_list, {'is_private': True}, name='my_events'),
    )