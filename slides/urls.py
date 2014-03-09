from django.conf.urls import patterns, url

from slides import views

urlpatterns = patterns('',
    url(r'^$', views.ListView.as_view(), name='index')
)