# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Slide.header'
        db.alter_column(u'slides_slide', 'header', self.gf('django.db.models.fields.CharField')(max_length=256))

    def backwards(self, orm):

        # Changing field 'Slide.header'
        db.alter_column(u'slides_slide', 'header', self.gf('django.db.models.fields.CharField')(max_length=128))

    models = {
        u'slides.section': {
            'Meta': {'ordering': "['order']", 'object_name': 'Section'},
            'colour_scheme': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        },
        u'slides.slide': {
            'Meta': {'ordering': "['order']", 'object_name': 'Slide'},
            'colour_scheme': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['slides.Section']"}),
            'slide_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'talk': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['slides.Talk']", 'blank': 'True'}),
            'time': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        },
        u'slides.talk': {
            'Meta': {'object_name': 'Talk'},
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'talk': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        }
    }

    complete_apps = ['slides']