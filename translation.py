from modeltranslation.translator import translator, TranslationOptions
from django.contrib.flatpages.models import FlatPage
from foto_report.models import Report, Images

class FlatPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

class ReportTranslationOptions(TranslationOptions):
    fields = ('excerpt', 'body')

class ImagesTranslationOptions(TranslationOptions):
    fields = ('name', 'excerpt', )

translator.register(FlatPage, FlatPageTranslationOptions)
translator.register(Report, ReportTranslationOptions)
translator.register(Images, ImagesTranslationOptions)
