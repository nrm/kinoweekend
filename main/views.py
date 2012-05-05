# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from main.models import Video, Report
from django.core.paginator import Paginator, EmptyPage, InvalidPage

import urllib2, urlparse, json

def index(request):
    videos = Video.objects.all()
    for video in videos:
        video.preview = _v_link(video.video_link)
    photo = get_or_none(Report, id=2)
    paginator = Paginator(videos, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        videos = paginator.page(page)
    except(EmptyPage, InvalidPage):
        videos = paginator.page(paginator.num_pages)

    return render_to_response('index.html', {'videos': videos, 'photo': photo},
            context_instance=RequestContext(request))

def image_details(request, slug):
    images = Report.objects.get(id=1)

    return render_to_response('image_detail.html', {'images': images},
            context_instance=RequestContext(request))


def details(request, slug):
    """@todo: Docstring for details
    """
    video = Video.objects.get(slug=slug)
    video.video = _get_video(video.video_link)

    return render_to_response('detail.html', {'video': video},
            context_instance=RequestContext(request))

def test2(request):
    return render_to_response('test2.html', {},
            context_instance=RequestContext(request))








def _v_link(link):
    type_link = urlparse.urlparse(link)
    if type_link.netloc == 'www.youtube.com':
        return 'http://img.youtube.com/vi/%s/0.jpg'%(type_link.query.split('v=')[-1].split('&')[0])
    elif type_link.netloc == 'vimeo.com':
        response = urllib2.urlopen('http://vimeo.com/api/v2/video/%s.json'%type_link.path.lstrip('/'))
        result = json.loads(response.read())[0]['thumbnail_medium']
        return result
    else:
        return 'http://placehold.it/200x125'

def _get_video(link):
    """@todo: Docstring for get_video
    """
    type_link = urlparse.urlparse(link)
    if type_link.netloc == 'www.youtube.com':
        return '<iframe width="720" height="396" src="http://www.youtube.com/embed/%s" frameborder="0" allowfullscreen></iframe>'%type_link.query.split('v=')[-1].split('&')[0]
    elif type_link.netloc == 'vimeo.com':
        return '<iframe src="http://player.vimeo.com/video/%s?byline=0&amp;portrait=0&amp;color=00a850" width="720" height="396" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>'%type_link.path.lstrip('/')

def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None
