# -*- coding: utf-8 -*-
from django.contrib import admin
from main.models import Video

class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        (None, {
            'fields': ('name', )
        }),
        (u'Описание', {
            'fields':('teaser', 'description', 'video_link'),
            }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('slug',)
        }),

)


admin.site.register(Video, VideoAdmin)
