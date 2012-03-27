from django.conf.urls.defaults import patterns, include, url
from settings import DEBUG, STATIC_ROOT, STATIC_URL

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

    url(r'^works/', 'main.views.index', name='works'),
    url(r'^$', 'news.views.news', name='home'),
    url(r'^news/$', 'news.views.news', name='news'),
    url(r'^news/(?P<slug>[-\w]+)/$', 'news.views.details', name='post'),

)

if DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
