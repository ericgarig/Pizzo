from django.conf.urls import patterns, url
from vacation_day import views

urlpatterns = patterns('',
	url(r'^$', views.VacationDayListView.as_view(), name='list'),
	url(r'^(?P<pk>\d+)/$', views.VacationDayDetailView.as_view(), name='detail'),
)