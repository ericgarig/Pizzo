from django.conf.urls import patterns, url
from attendance import views

urlpatterns = patterns('',
	url(r'^inventory/$', views.AttendanceListView.as_view(), name='list'),
	url(r'^(?P<pk>\d+)/$', views.AttendanceDetailView.as_view(), name='detail'),
)