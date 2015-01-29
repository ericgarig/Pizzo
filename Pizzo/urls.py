from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView

# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^projects/', include('PizzoDB.urls', namespace="PizzoDB")),
	



	#url(r'^$', include('PizzoDB.urls', namespace="PizzoDB"))

	
	# url(r'^$', 'PizzoDB.views.home'),
	# url(r'^polls/', include('polls.urls', namespace="polls")),
	# url(r'^blog/', include('blog.urls')),
		# ('^$', now),
		# ('^hello/$', hello),
	


	# Examples:
	# url(r'^$', 'Pizzo.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
)
