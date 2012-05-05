from modeltranslation.translator import translator, TranslationOptions
from django.contrib.flatpages.models import FlatPage
#from foto_report.models import Report, Images
from main.models import Video, Report, Images
from news.models import Post

class FlatPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

class ReportTranslationOptions(TranslationOptions):
    fields = ('excerpt', 'body')

class ImagesTranslationOptions(TranslationOptions):
    fields = ('name', 'excerpt', )

class VideoTranslationOptions(TranslationOptions):
    fields = ('name', 'authors', 'teaser', 'description', 'prize','city',)

class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'excerpt', 'body')

translator.register(FlatPage, FlatPageTranslationOptions)
translator.register(Report, ReportTranslationOptions)
translator.register(Images, ImagesTranslationOptions)
translator.register(Video, VideoTranslationOptions)
translator.register(Post, PostTranslationOptions)
