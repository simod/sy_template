from django.template import RequestContext
from django.shortcuts import render_to_response

from geonode.layers.models import Layer
from geonode.maps.models import Map
from geonode.documents.models import Document
from geonode.people.models import Profile
from geonode.search.views import search_api

focus_areas = [
    {'Aleppo': {
            'keyword': 'aleppo',
            'img': 'aleppo.png'
        }},
    {'Homs': {
            'keyword': 'homs',
            'img': 'homs.png'
        }},
    {'Damascus': {
            'keyword': 'damascus',
            'img': 'damascus.png'
        }},
    {'Hama': {
            'keyword': 'hama',
            'img': 'hama.png'
        }},
    {'Al Qusayr': {
            'keyword': 'al_qusayr',
            'img': 'al_qusayr.png'
        }},
    {'Duma': {
            'keyword': 'duma',
            'img': 'duma.png'
        }},
    {'Deir Ez-Zor': {
            'keyword': 'deir_ez_zor',
            'img': 'deir_ez_zor.png'
        }},
    {'Idlib': {
            'keyword': 'idlib',
            'img': 'idlib.png'
        }},
    {'Az Zabadani': {
            'keyword': 'az_zabadani',
            'img': 'az_zabadani.png'
        }},
    {'Ar Raqqah': {
            'keyword': 'ar_raqqah',
            'img': 'ar_raqqah.png'
        }},
    {'A\'zaz': {
            'keyword': 'azaz',
            'img': 'azaz.png'
        }},
    {'Syria': {
            'keyword': 'syria',
            'img': 'focus_syria.png'
        }},
]

def index(request, template='index.html'):
    post = request.POST.copy()
    post.update({'type': 'layer'})
    request.POST = post
    return search_page(request, template=template)


def search_page(request, template='search/search.html', **kw): 
    results, facets, query = search_api(request, format='html', **kw)

    facets = {      
        'maps' : Map.objects.count(),
        'layers' : Layer.objects.count(),
        'documents': Document.objects.count(),
        'users' : Profile.objects.count()
    }
    
    return render_to_response(template, RequestContext(request, {'object_list': results, 
        'facets': facets, 'total': facets['layers'], 'focus_areas': focus_areas}))
