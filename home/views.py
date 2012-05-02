# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from home.models import DjangoApplication

def intro(request):
    return render_to_response('intro.html', {},
            context_instance=RequestContext(request))

def festival(request):
    print request
    return render_to_response('festival.html', {},
            context_instance=RequestContext(request))

def home(request):
    print request.LANGUAGE_CODE
    posts = DjangoApplication.objects.language('%s'%request.LANGUAGE_CODE).all()
    #text = DjangoApplication.objects.language('%s'%request.LANGUAGE_CODE).filter(description_author='Jonas Obrist')
    #posts = Post.objects.get_visible()[0:5]

    return render_to_response('home.html', {'posts': posts},
            context_instance=RequestContext(request))
