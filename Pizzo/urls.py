from django.conf.urls import patterns, include, url
from django.contrib import admin

from Pizzo import views


urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^attendance/', include('attendance.urls', namespace="attendance")),
	url(r'^employee/', include('employee.urls', namespace="employee")),
	url(r'^material/', include('material.urls', namespace="material")),
	url(r'^vacation_day/', include('vacation_day.urls', namespace="vacation_day")),
	url(r'^', include('PizzoDB.urls', namespace="PizzoDB")),


	url(r'^hello/$', views.hello),
)
