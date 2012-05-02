# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Video.name_ru'
        db.add_column('main_video', 'name_ru', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Video.name_en'
        db.add_column('main_video', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Video.authors_ru'
        db.add_column('main_video', 'authors_ru', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Video.authors_en'
        db.add_column('main_video', 'authors_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Video.teaser_ru'
        db.add_column('main_video', 'teaser_ru', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Video.teaser_en'
        db.add_column('main_video', 'teaser_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Video.description_ru'
        db.add_column('main_video', 'description_ru', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Video.description_en'
        db.add_column('main_video', 'description_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Images.name_ru'
        db.add_column('main_images', 'name_ru', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'Images.name_en'
        db.add_column('main_images', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'Images.excerpt_ru'
        db.add_column('main_images', 'excerpt_ru', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Images.excerpt_en'
        db.add_column('main_images', 'excerpt_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Report.excerpt_ru'
        db.add_column('main_report', 'excerpt_ru', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Report.excerpt_en'
        db.add_column('main_report', 'excerpt_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Report.body_ru'
        db.add_column('main_report', 'body_ru', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Report.body_en'
        db.add_column('main_report', 'body_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Video.name_ru'
        db.delete_column('main_video', 'name_ru')

        # Deleting field 'Video.name_en'
        db.delete_column('main_video', 'name_en')

        # Deleting field 'Video.authors_ru'
        db.delete_column('main_video', 'authors_ru')

        # Deleting field 'Video.authors_en'
        db.delete_column('main_video', 'authors_en')

        # Deleting field 'Video.teaser_ru'
        db.delete_column('main_video', 'teaser_ru')

        # Deleting field 'Video.teaser_en'
        db.delete_column('main_video', 'teaser_en')

        # Deleting field 'Video.description_ru'
        db.delete_column('main_video', 'description_ru')

        # Deleting field 'Video.description_en'
        db.delete_column('main_video', 'description_en')

        # Deleting field 'Images.name_ru'
        db.delete_column('main_images', 'name_ru')

        # Deleting field 'Images.name_en'
        db.delete_column('main_images', 'name_en')

        # Deleting field 'Images.excerpt_ru'
        db.delete_column('main_images', 'excerpt_ru')

        # Deleting field 'Images.excerpt_en'
        db.delete_column('main_images', 'excerpt_en')

        # Deleting field 'Report.excerpt_ru'
        db.delete_column('main_report', 'excerpt_ru')

        # Deleting field 'Report.excerpt_en'
        db.delete_column('main_report', 'excerpt_en')

        # Deleting field 'Report.body_ru'
        db.delete_column('main_report', 'body_ru')

        # Deleting field 'Report.body_en'
        db.delete_column('main_report', 'body_en')


    models = {
        'main.images': {
            'Meta': {'object_name': 'Images'},
            'excerpt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'excerpt_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'excerpt_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Report']"})
        },
        'main.report': {
            'Meta': {'object_name': 'Report'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'body_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'body_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'excerpt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'excerpt_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'excerpt_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preview': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'main.video': {
            'Meta': {'object_name': 'Video'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'authors_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'authors_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'teaser': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'teaser_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'teaser_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'video_link': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['main']
