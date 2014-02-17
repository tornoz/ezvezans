from django.conf.urls import patterns, url

from abs import views

urlpatterns = patterns('',
    url(r'^login/', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page':'/abs/login'}),
    url(r'^add/(?P<entity>\w+)', views.add, name='add'),
    url(r'^ajax/absent/(?P<coursid>\d+)', views.ajax_absent, name='ajax_absent'),
    url(r'^$', views.index, name='index')
)
