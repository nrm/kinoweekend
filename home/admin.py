# -*- coding: utf-8 -*-
from django.contrib import admin
from home.models import DjangoApplication #, Normal, SimpleRelated, LimitedChoice
from nani.admin import TranslatableAdmin, TranslatableTabularInline


from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from modeltranslation.admin import TranslationAdmin

class MyFlatPageAdmin(TranslationAdmin):
    class Media:
        js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

class MyFlatPageAdmin(MyFlatPageAdmin, TranslationAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(MyFlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        self.patch_translation_field(db_field, field, **kwargs)
        return field

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, MyFlatPageAdmin)


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

