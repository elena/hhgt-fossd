from django.conf.urls import patterns, url

from slides import views

urlpatterns = patterns('',
    url(r'^section/(?P<pk>\d+)/$', views.SectionDetailView.as_view(),
        name='section_detail_view'),

    url(r'^$', views.ListView.as_view(), name='index'),
)