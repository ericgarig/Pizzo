from django.conf.urls import patterns, url
from PizzoDB import views

urlpatterns = patterns('',
	# url(r'^$', ProjectListView.as_view(), name='home'),
	url(r'^$', views.index, name='index'),
	url(r'^(?P<project_id>\d+)/$', views.detail, name='project'),


    # url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/results$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name='vote'),
)