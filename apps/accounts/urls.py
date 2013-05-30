from django.conf.urls import patterns, url


from accounts import views

urlpatterns = patterns('',
    url(r'^register/$', views.register, name='register'),
    #url(r'^login/$', views.login, name='login')
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/auth.html'},name='login'),
    url(r'^password_reset/$','django.contrib.auth.views.password_reset',{'template_name':'accounts/password_reset_form.html'}, name='password_reset'),
    url(r'^password_reset_confirm/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$','django.contrib.auth.views.password_reset_confirm',{'template_name':'accounts/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^password_reset_done/$','django.contrib.auth.views.password_reset_done',{'template_name':'accounts/password_reset_done.html'}, name='password_reset_done'),
    url(r'^password_reset_complete/$','django.contrib.auth.views.password_reset_complete',{'template_name':'accounts/password_reset_complete.html'}, name='password_reset_complete'),
    url(r'^user_edit/$',views.user_edit,name='user_edit')
)
