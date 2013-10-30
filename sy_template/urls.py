from django.conf.urls import patterns, url, include

from geonode.urls import urlpatterns

urlpatterns = patterns('',

    # Static pages
    url(r'^$', 'sy_template.views.index', {'template': 'site_index.html'}, name='home'),
 
 ) + \
urlpatterns + \
patterns('',
    (r'^formhub/', include('geonode_formhub.urls')),
)