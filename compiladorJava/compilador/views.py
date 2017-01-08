from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from compilador.models import *
from django.http import HttpResponse, Http404
from django.core import serializers
import json

# Create your views here.

def index_view(request):
	return render_to_response('index.html', context=RequestContext(request))
