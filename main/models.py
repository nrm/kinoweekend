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
    teaser = models.TextField(blank=True,
                                  help_text="Короткое описание ролика")
    slug = models.SlugField()
    description = models.TextField(blank=True,
                                  help_text="Describe your video.")
    youtube_link = models.TextField(blank=False,
                            help_text=u"Ссылка на youtube видео. Под роликом в youtube кнопка 'Поделиться' -> 'Сгенерировать HTML-код, получившееся вставляем в это окно'")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Видео'
        verbose_name_plural = u'Видео'
