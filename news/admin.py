from news.models import Post
from django.contrib import admin
#from settings import STATIC_URL, STATIC_ROOT
#from django.contrib.admin import site, ModelAdmin


#from django.core.urlresolvers import reverse
#from django.contrib.flatpages.admin import FlatPageAdmin
#from django.contrib.flatpages.models import FlatPage
#from tinymce.widgets import TinyMCE

##class CommonMedia:
##    js = (
##        'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
##        '%sjs/editor.js'%STATIC_URL,
##        )
##    css = {
##        #'all': ('%scss/editor.css'%STATIC_URL,),
##        #'all': ('/site_media/css/editor.css',),
##        }
##

#class TinyMCEFlatPageAdmin(FlatPageAdmin):
#    def formfield_for_dbfield(self, db_field, **kwargs):
#        if db_field.name == 'content':
#            return forms.CharField(widget=TinyMCE(
#                attrs={'cols': 80, 'rows': 30},
#                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
#            ))
#        return super(TinyMCEFlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)
#
#
#class PostForm(forms.ModelForm):
#    excerpt = forms.CharField( widget=CKEditor(ckeditor_config='default'))
#    #body = forms.CharField( widget=CKEditor(ckeditor_config='full'))
#    body = forms.CharField(widget=TinyMCE())
#
#    class Meta:
#        model = Post

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
    #form = PostForm

admin.site.register(Post, PostAdmin)

#admin.site.unregister(FlatPage)
#admin.site.register(FlatPage, TinyMCEFlatPageAdmin)
