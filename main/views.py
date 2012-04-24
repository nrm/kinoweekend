# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from main.models import Video

def test(request):
    return render_to_response('test.html', {},
            context_instance=RequestContext(request))

def intro(request):
    return render_to_response('intro.html', {},
            context_instance=RequestContext(request))

def index(request):
    videos = Video.objects.all()

    return render_to_response('index.html', {'videos': videos},
            context_instance=RequestContext(request))
