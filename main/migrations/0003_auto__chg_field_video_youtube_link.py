# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Video.youtube_link'
        db.alter_column('main_video', 'youtube_link', self.gf('django.db.models.fields.TextField')())


    def backwards(self, orm):
        
        # Changing field 'Video.youtube_link'
        db.alter_column('main_video', 'youtube_link', self.gf('django.db.models.fields.CharField')(max_length=255))


    models = {
        'main.video': {
            'Meta': {'object_name': 'Video'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'youtube_link': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['main']
