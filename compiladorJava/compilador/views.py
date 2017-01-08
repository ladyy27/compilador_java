# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
# Create your views here.
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from json import JSONEncoder
from compilador.models import *
import json

# Create your views here.

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request));
