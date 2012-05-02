# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Video.city'
        db.add_column('main_video', 'city', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True), keep_default=False)

        # Adding field 'Video.city_ru'
        db.add_column('main_video', 'city_ru', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Video.city_en'
        db.add_column('main_video', 'city_en', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Changing field 'Video.prize_ru'
        db.alter_column('main_video', 'prize_ru', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Video.prize_en'
        db.alter_column('main_video', 'prize_en', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Video.prize'
        db.alter_column('main_video', 'prize', self.gf('django.db.models.fields.CharField')(max_length=100))


    def backwards(self, orm):
        
        # Deleting field 'Video.city'
        db.delete_column('main_video', 'city')

        # Deleting field 'Video.city_ru'
        db.delete_column('main_video', 'city_ru')

        # Deleting field 'Video.city_en'
        db.delete_column('main_video', 'city_en')

        # Changing field 'Video.prize_ru'
        db.alter_column('main_video', 'prize_ru', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Video.prize_en'
        db.alter_column('main_video', 'prize_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Video.prize'
        db.alter_column('main_video', 'prize', self.gf('django.db.models.fields.CharField')(max_length=255))


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
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'city_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city_ru': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'prize': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'prize_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'prize_ru': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'teaser': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'teaser_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'teaser_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'video_link': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['main']
