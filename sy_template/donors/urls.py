from django.conf.urls import patterns, url, include


urlpatterns = patterns('',
    url(r'^mapping/?$', 'sy_template.donors.views.donors_mapping', { 'template': 'donors/donors_mapping.html'}, name='donors_mapping'),
    url(r'^meeting/?$', 'sy_template.donors.views.donors_mapping', { 'template': 'donors/donors_meeting.html'}, name='donors_meeting'),
 ) 