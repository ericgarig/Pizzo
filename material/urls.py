from django.conf.urls import patterns, url

from material import views

urlpatterns = patterns('',
	url(r'^inventory/$', views.InventoryListView.as_view(), name='list'),
	url(r'^inventory/(?P<pk>\d+)/$', views.InventoryDetailView.as_view(), name='detail'),

	url(r'^$', views.MaterialListView.as_view(), name='list'),
	url(r'^(?P<pk>\d+)/$', views.MaterialDetailView.as_view(), name='detail'),
)