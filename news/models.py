# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostManager(models.Manager):
    def get_visible(self):
        return self.get_query_set().filter(publish_at__lte=datetime.datetime.now(), active=True)


class TimeStampedActivate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False,
                                 help_text="Controls whether or not this item is live to the world.")

    class Meta:
        abstract = True


class Post(TimeStampedActivate):
    """
    A news post that belongs to a Newsletter.

    >>> p = Post()
    >>> p.title = "A Test Post"
    >>> p.user = User.objects.create(username='foo', password='test')
    >>> p.body = "Just a small test"
    >>> p.slug = "a-test-post"
    >>> p.save()
    >>> print p.title
    A Test Post
    >>> print p.active
    False
    >>> print p.user.username
    foo
    """
    title = models.CharField(max_length=255,
                             help_text="Title of the news. Can be anything up to 255 characters.")
    user = models.ForeignKey(User)
    slug = models.SlugField()
    excerpt = models.TextField(blank=True,
                               help_text="A small teaser of your content")
    body = models.TextField()
    publish_at = models.DateTimeField(default=datetime.datetime.now(),
                                     help_text="Date and time post should become visible.")
    #blog = models.ForeignKey(Blog, related_name="posts")
    #tags = TaggableManager()
    objects = PostManager()

    #def get_absolute_url(self):
    #    return "/news/%s/" % self.slug

    @models.permalink
    def get_absolute_url(self):
        #return ('main.views.index', self.slug)
        #return ('post', self.slug)
        # return "/main/%s/" % self.slug
        return ('post', {}, {'slug': self.slug})

    def is_visible(self):
        """
        Checks to see if a post is supposed be visible when accessed outside
        of a queryset.
        """
        if self.active and self.publish_at <= datetime.datetime.now():
            return True
        return False

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-publish_at"]
        verbose_name = u"Новость"
        verbose_name_plural = "Новости"

