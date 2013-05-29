from django.conf.urls import patterns, url


from accounts import views

urlpatterns = patterns('',
    url(r'^register/$', views.register, name='register'),
    #url(r'^login/$', views.login, name='login')
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/auth.html'},name='login'),


    
)
