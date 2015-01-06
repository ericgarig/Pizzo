from django.conf.urls import patterns, include, url
from django.contrib import admin
from Pizzo.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Pizzo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^blog/', include('blog.urls', namespace="blog")),
        ('^$', now),
        ('^hello/$', hello),
)
