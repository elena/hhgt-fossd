# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Section.order'
        db.alter_column(u'slides_section', 'order', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Slide.time'
        db.alter_column(u'slides_slide', 'time', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Slide.order'
        db.alter_column(u'slides_slide', 'order', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Section.order'
        raise RuntimeError("Cannot reverse this migration. 'Section.order' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Section.order'
        db.alter_column(u'slides_section', 'order', self.gf('django.db.models.fields.IntegerField')())

        # User chose to not deal with backwards NULL issues for 'Slide.time'
        raise RuntimeError("Cannot reverse this migration. 'Slide.time' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Slide.time'
        db.alter_column(u'slides_slide', 'time', self.gf('django.db.models.fields.IntegerField')())

        # User chose to not deal with backwards NULL issues for 'Slide.order'
        raise RuntimeError("Cannot reverse this migration. 'Slide.order' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Slide.order'
        db.alter_column(u'slides_slide', 'order', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'slides.section': {
            'Meta': {'ordering': "['order']", 'object_name': 'Section'},
            'colour_scheme': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        },
        u'slides.slide': {
            'Meta': {'ordering': "['order']", 'object_name': 'Slide'},
            'colour_scheme': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['slides.Section']"}),
            'slide_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'talk': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['slides.Talk']", 'blank': 'True'}),
            'time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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