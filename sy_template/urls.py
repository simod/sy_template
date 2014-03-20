from django.conf.urls import patterns, url, include

from geonode.urls import urlpatterns

urlpatterns = patterns('',

    # Static pages
    url(r'^$', 'sy_template.views.index', {'template': 'site_index.html'}, name='home'),
    url(r'^areas_search/?$', 'sy_template.views.search_page', {'template': 'search/areas_search.html'}, name='areas_search'),
 
 ) + \
urlpatterns + \
patterns('',
    (r'^formhub/', include('geonode_formhub.urls')),
)