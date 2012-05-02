from django.db import models

# Create your models here.

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

class Images(models.Model):
    report = models.ForeignKey(Report)
    name = models.CharField(max_length=200,
                             help_text="Title of the image. Can be anything up to 255 characters.")
    excerpt = models.CharField(blank=True, max_length=255,
                               help_text="A small teaser of your image")
    image = models.ImageField(upload_to='foto_report')

    def __unicode__(self):
        return self.name
