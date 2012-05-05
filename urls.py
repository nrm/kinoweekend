from django.conf.urls.defaults import patterns, include, url
from settings import DEBUG, STATIC_ROOT, STATIC_URL, MEDIA_ROOT, MEDIA_URL


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'source.views.home', name='home'),
    # url(r'^source/', include('source.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^localeurl/', include('localeurl.urls')),

    #url(r'^$', 'home.views.intro', name='intro'),
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/about'}),
    (r'^reg/$', 'django.views.generic.simple.direct_to_template', {'template': 'reg.html'}),
    url(r'^news/$', 'news.views.news', name='news'),
    url(r'^news/(?P<slug>[-\w]+)/$', 'news.views.details', name='post'),
    url(r'^works/$', 'main.views.index', name='works'),
    url(r'^works/(?P<slug>[-\w]+)/$', 'main.views.details', name='video'),
    url(r'^photo/(?P<slug>[-\w]+)/$', 'main.views.image_details', name='photo'),

)

if DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
