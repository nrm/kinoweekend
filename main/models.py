# -*- coding: utf-8 -*-
from django.db import models
# Create your models here.

class TimeStampedActivate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False,
                                 help_text="Controls whether or not this item is live to the world.")

    class Meta:
        abstract = True

class Video(TimeStampedActivate):
    """
    A blog belonging to a user.
    Blogs have multiple posts and one user can have many blogs.
    """
    name = models.CharField(max_length=255,
                           help_text="Name of your Video. Can be anything up to 255 characters.")
    slug = models.SlugField()
    authors = models.CharField(max_length=255,
                           help_text="Author of your Video. Can be anything up to 255 characters.")
    city = models.CharField(max_length=100, blank=True,
                           help_text="City.  Может быть пустой.")
    prize = models.CharField(max_length=100, blank=True,
                           help_text="Prize of your Video. Может быть пустой.")
    teaser = models.TextField(blank=True,
                                  help_text="Короткое описание ролика")
    description = models.TextField(blank=True,
                                  help_text="Describe your video.")
    video_link = models.CharField(max_length=255,
                            help_text=u"Ссылка на видео.")

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('video', {}, {'slug': self.slug})


    class Meta:
        verbose_name = u'Видео'
        verbose_name_plural = u'Видео'


class Report(models.Model):
    title = models.CharField(max_length=200,
                             help_text="Title of the report. Can be anything up to 255 characters.")
    slug = models.SlugField()
    pub_date = models.DateTimeField('date published')
    excerpt = models.TextField(blank=True,
                               help_text="A small teaser of your content")
    body = models.TextField(blank=True,
                               help_text="A text of your content")
    preview = models.ImageField(upload_to='foto_report',
                               help_text="preview image of your report")

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('photo', {}, {'slug': self.slug})

    class Meta:
        verbose_name = u'Фото отчет'
        verbose_name_plural = u'Фото отчеты'



class Images(models.Model):
    report = models.ForeignKey(Report)
    name = models.CharField(max_length=200,
                             help_text="Title of the image. Can be anything up to 255 characters.")
    excerpt = models.CharField(blank=True, max_length=255,
                               help_text="A small teaser of your image")
    image = models.ImageField(upload_to='foto_report')


    def __unicode__(self):
        return self.name
