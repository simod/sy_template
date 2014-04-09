from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from .models import DonorsMapping

@login_required
def donors_mapping(request, template='donors/donors_mapping.html'):
    the_filter = 'mapping' if 'mapping' in template else 'meeting'
    mappings = DonorsMapping.objects.filter(type=the_filter)
    return render_to_response(template, RequestContext(request, { 
         'mappings': mappings, }))