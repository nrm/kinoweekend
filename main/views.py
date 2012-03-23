# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from main.models import Video

def index(request):
    videos = Video.objects.all()

    return render_to_response('main/index.html', {'videos': videos},
            context_instance=RequestContext(request))
