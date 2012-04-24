# -*- coding: utf-8 -*-
from django.contrib import admin
from home.models import DjangoApplication #, Normal, SimpleRelated, LimitedChoice
from nani.admin import TranslatableAdmin, TranslatableTabularInline

class DjangoApplicationAdmin(TranslatableAdmin):
    model = DjangoApplication

    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'author')
    list_display_links = ('name',)
    ###list_filter = ('publish_at', 'modified', 'created', 'active')
    ###date_hierarchy = 'publish_at'
    ###search_fields = ['title', 'excerpt', 'body', 'user']
    #fieldsets = (
    #    (None, {
    #        'fields': ('name', 'author'),
    #    }),
    #    ('Content', {
    #        'fields': ('teaser', 'description'),
    #        'description': "Это часть данных которая отображается на странице и требует перевода.",
    #    }),
    #    ('Optional', {
    #        'fields': ('slug',),
    #        'classes': ('collapse',),
    #    })
    #)


admin.site.register(DjangoApplication, DjangoApplicationAdmin)

    #inlines = [DjangoApplication,]

#class SimpleRelatedInline(TranslatableTabularInline):
#    model = DjangoApplication

#class NormalAdmin(TranslatableAdmin):
#    inlines = [SimpleRelatedInline,]

##admin.site.register(Normal, NormalAdmin)
##admin.site.register(SimpleRelated, TranslatableAdmin)
#admin.site.register(DjangoApplication, TranslatableAdmin)
