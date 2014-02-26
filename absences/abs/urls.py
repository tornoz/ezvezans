from django.conf.urls import patterns, url

from abs import views

urlpatterns = patterns('',
    url(r'^login/', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page':'/abs/login'}),
    url(r'^add/(?P<entity>\w+)', views.add, name='add'),
    url(r'^ajax/absent/(?P<coursid>\d+)', views.ajax_absent, name='ajax_absent'),
    url(r'^ajax/insert/absent/(?P<coursid>\d+)/(?P<etudiantid>\w+)', views.ajax_insert_absent, name='ajax_insert_absent'),
    url(r'^ajax/delete/(?P<table>\w+)/(?P<id>\d+)', views.ajax_delete, name='ajax_delete'),
    url(r'^validate/(?P<justid>\d+)', views.validate_justificatif, name='valdate_justificatif'),
    url(r'^$', views.index, name='index')
)
