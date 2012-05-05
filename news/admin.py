from news.models import Post
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('active', 'title', 'publish_at', 'user')
    list_display_links = ('title',)
    list_editable = ('active',)
    list_filter = ('publish_at', 'modified', 'created', 'active')
    date_hierarchy = 'publish_at'
    search_fields = ['title', 'excerpt', 'body', 'user']
    fieldsets = (
        (None, {
            'fields': ('title', 'user'),
        }),
        ('Publication', {
            'fields': ('active', 'publish_at'),
            'description': "Control <strong>whether</strong> and <strong>when</strong> a post is visible to the world.",
        }),
        ('Content', {
            'fields': ('excerpt', 'body'),
        }),
        ('Optional', {
            'fields': ('slug',),
            'classes': ('collapse',),
        })
    )

    class Media:
        js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

class TranslatedPostAdmin(PostAdmin, TranslationAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(TranslatedPostAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        self.patch_translation_field(db_field, field, **kwargs)
        return field

admin.site.register(Post, TranslatedPostAdmin)

