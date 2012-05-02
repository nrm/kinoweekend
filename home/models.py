# -*- coding: utf-8 -*-
from django.db import models
from nani.models import TranslatableModel, TranslatedFields
from django.contrib.auth.models import User

# Create your models here.

class DjangoApplication(TranslatableModel):
    author = models.ForeignKey(User)
    slug = models.SlugField()
    name = models.CharField(max_length=255,
                           help_text="Name of page. Can be anything up to 255 characters.")

    translations = TranslatedFields(
        title = models.CharField(max_length=255,
                               help_text="Name of title. Can be anything up to 255 characters."),
        teaser = models.TextField(blank=True,
                                      help_text="Короткое описание"),
        description = models.TextField(blank=True,
                                      help_text="Main text describe."),
    )

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('home', {}, {'slug': self.slug})

    class Meta:
        verbose_name = u"О фестивале"
        verbose_name_plural = "О Фестивале"
