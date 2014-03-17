# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Slide.bg_img'
        db.add_column(u'slides_slide', 'bg_img',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=256, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Slide.bg_img'
        db.delete_column(u'slides_slide', 'bg_img')


    models = {
        u'slides.section': {
            'Meta': {'ordering': "['order']", 'object_name': 'Section'},
            'colour_scheme': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'talk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['slides.Talk']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        },
        u'slides.slide': {
            'Meta': {'ordering': "['section__order', 'order']", 'object_name': 'Slide'},
            'bg_img': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'colour_scheme': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'percent_complete': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '32', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['slides.Section']"}),
            'slide_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'talk': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['slides.Talk']", 'blank': 'True'}),
            'time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'versionA': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'versionB': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'versionC': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'slides.talk': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Talk'},
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'talk': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        },
        u'slides.version': {
            'Meta': {'object_name': 'Version'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['slides']