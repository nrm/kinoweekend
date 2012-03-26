# Create your views here.
from django.shortcuts import render_to_response, get_list_or_404 #, get_object_or_404
from news.models import Post
from django.template import RequestContext

def index(request):
    posts = get_list_or_404(Post.objects.get_visible())[0:5]

    return render_to_response('main/index.html', {'posts': posts},
            context_instance=RequestContext(request))

def news(request):
    #posts = get_list_or_404(Post.objects.get_visible())[0:5]
    posts = Post.objects.get_visible()[0:5]

    return render_to_response('news/news.html', {'posts': posts},
            context_instance=RequestContext(request))

#def details(request, slug):
#    """docstring for details"""
#    #post = Post.objects.get_visible().get(slug=slug)
#
#    post = get_object_or_404(Post.objects.get_visible(), slug=slug)
#
#    # Get an instance of a logger
#    #logger = logging.getLogger(__name__)
#    #logger.error('There was some crazy error and post is %s'%post.title,
#    #             exc_info=True,
#    #             extra={'request': request,})
#
#    #post = get_object_or_404(Post.objects.get_visible().get(slug=slug))
#
#    #return list_detail.object_detail(request, queryset, slug=slug)
#    return render_to_response('main/details.html', {'post': post},
#            context_instance=RequestContext(request))
#
#def test(request):
#    posts = Post.objects.get_visible()[0:5]
#
#    return render_to_response('index.html', {'posts': posts},
#            context_instance=RequestContext(request))
