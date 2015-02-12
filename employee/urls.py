from django.conf.urls import patterns, url
from employee import views

urlpatterns = patterns('',
	url(r'^$', views.EmployeeListView.as_view(), name='employee_list'),
	url(r'^(?P<pk>\d+)/$', views.EmployeeDetailView.as_view(), name='employee'),



	# """test"""
	# url(r'^projects/(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name='project'),



    # url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/results$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name='vote'),
)