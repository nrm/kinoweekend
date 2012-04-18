# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from main.models import Video

def intro(request):
    return render_to_response('main/intro.html', {},
            context_instance=RequestContext(request))

def test(request):
    return render_to_response('main/test.html', {},
            context_instance=RequestContext(request))

def test2(request):
    return render_to_response('main/test2.html', {},
            context_instance=RequestContext(request))

def index(request):
    videos = Video.objects.all()

    return render_to_response('main/index.html', {'videos': videos},
            context_instance=RequestContext(request))
