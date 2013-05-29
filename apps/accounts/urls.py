from django.conf.urls import patterns, url


from accounts import views

urlpatterns = patterns('',
    url(r'^registration/$', views.register, name='register')
)
