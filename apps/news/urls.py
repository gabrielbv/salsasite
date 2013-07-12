from django.conf.urls import patterns, url


from news import views

urlpatterns = patterns('',

	url(r'^add/$', views.add, name='add'),
	url(r'^$', views.list, name='list')

)