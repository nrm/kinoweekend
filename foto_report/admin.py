# -*- coding: utf-8 -*-
from django.contrib import admin
from foto_report.models import Report, Images
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

class MyImagesAdmin(TranslationAdmin):
    class Media:
        js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

class ImageInline(TranslationTabularInline):
    model = Images

class MyReportAdmin(TranslationAdmin):
    """Docstring for MyReportAdmin """
    list_display = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = [
        (None,               {'fields': ['title', 'pub_date', 'excerpt', 'body', 'preview']}),
        ('Optional', {'fields': ['slug'], 'classes': ['collapse']}),
    ]
    inlines = [ImageInline,]

    class Media:
        js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

class TranslatedReportAdmin(MyReportAdmin, TranslationAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(TranslatedReportAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        self.patch_translation_field(db_field, field, **kwargs)
        return field


#class ReportAdmin(admin.ModelAdmin):
#    model = Report
#    prepopulated_fields = {"slug": ("title",)}
#    fieldsets = [
#        (None,               {'fields': ['title', 'pub_date', 'excerpt', 'body', 'preview']}),
#        ('Optional', {'fields': ['slug'], 'classes': ['collapse']}),
#    ]
#    inlines = [ImageInline]

admin.site.register(Report, TranslatedReportAdmin)
#admin.site.register(Report, ReportAdmin)
