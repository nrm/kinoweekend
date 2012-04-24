# Create your views here.
from django.shortcuts import render_to_response, get_list_or_404 , get_object_or_404
from news.models import Post
from django.template import RequestContext

def news(request):
    posts = Post.objects.get_visible().order_by('-publish_at')

    #posts = Post.objects.get_visible()[0:5]

    return render_to_response('news.html', {'posts': posts},
            context_instance=RequestContext(request))

def details(request, slug):
    """docstring for details"""
    post = get_object_or_404(Post.objects.get_visible(), slug=slug)

    return render_to_response('details.html', {'post': post},
            context_instance=RequestContext(request))

#def test(request):
#    posts = Post.objects.get_visible()[0:5]
#
#    return render_to_response('index.html', {'posts': posts},
#            context_instance=RequestContext(request))
