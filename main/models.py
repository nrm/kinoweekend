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
