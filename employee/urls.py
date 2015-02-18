from django.conf.urls import patterns, url

from employee import views

urlpatterns = patterns('',
	url(r'^$', views.EmployeeListView.as_view(), name='employee_list'),
	url(r'^(?P<pk>\d+)/$', views.EmployeeDetailView.as_view(), name='employee'),
)