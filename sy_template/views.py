from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils.datastructures import SortedDict

from geonode.layers.models import Layer
from geonode.maps.models import Map
from geonode.documents.models import Document
from geonode.people.models import Profile
from geonode.search.views import search_api

focus_areas = SortedDict([
    ('aleppo', {
            'name': 'Aleppo',
            'img': 'aleppo.png'
        }),
    ('homs', {
            'name': 'Homs',
            'img': 'homs.png'
        }),
    ('damascus', {
            'name': 'Damascus',
            'img': 'damascus.png'
        }),
    ('hama', {
            'name': 'Hama',
            'img': 'hama.png'
        }),
    ('al_qusayr', {
            'name': 'Al Qusayr',
            'img': 'al_qusayr.png'
        }),
    ('duma', {
            'name': 'Duma',
            'img': 'duma.png'
        }),
    ('deir_ez_zor', {
            'name': 'Deir Ez-Zor',
            'img': 'deir_ez_zor.png'
        }),
    ('idlib', {
            'name': 'Idlib',
            'img': 'idlib.png'
        }),
    ('az_zabadani', {
            'name': 'Az Zabadani',
            'img': 'az_zabadani.png'
        }),
    ('ar_raqqah', {
            'name': 'Ar Raqqah',
            'img': 'ar_raqqah.png'
        }),
    ('azaz', {
            'name': 'A\'zaz',
            'img': 'azaz.png'
        }),
    ('daraa', {
            'name': 'Daraa',
            'img': 'daraa.png'
        }),
    ('syria', {
            'name': 'Syria',
            'img': 'focus_syria.png'
        })
])

def index(request, template='site_index.html'):
    
    results, facets, query = search_api(request, format='html')

    return render_to_response(template, RequestContext(request, { 
        'facets': facets, 'focus_areas': focus_areas, }))


def search_page(request, template='search/search.html', **kw): 
    results, facets, query = search_api(request, format='html', **kw)
    keyword = request.REQUEST.get('kw','')
    
    total = 0
    for val in facets.values(): total+=val
    total -= facets['raster'] + facets['vector']

    return render_to_response(template, RequestContext(request, {'object_list': results, 
        'facets': facets, 'total': total, 'keyword': keyword, 
        'title': focus_areas[keyword]['name'] }))
