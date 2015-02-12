from django.conf.urls import patterns, url
from PizzoDB import views

urlpatterns = patterns('',
	url(r'^$', views.ProjectListView.as_view(), name='list'),
	url(r'^project/(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name='detail'),


	
)