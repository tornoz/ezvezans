from django.conf.urls import patterns, url

from abs import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
