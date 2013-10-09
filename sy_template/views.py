from django.template import RequestContext
from django.shortcuts import render_to_response

from geonode.layers.models import Layer
from geonode.maps.models import Map
from geonode.documents.models import Document
from geonode.people.models import Profile
from geonode.search.views import search_api

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
        'facets': facets, 'total': facets['layers']}))
