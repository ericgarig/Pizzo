from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', 'blog.views.index'),
    url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post'),
]