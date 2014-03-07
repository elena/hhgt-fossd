# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Talk'
        db.create_table(u'slides_talk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('talk', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('event', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
        ))
        db.send_create_signal(u'slides', ['Talk'])


        # Renaming column for 'Slide.talk' to match new field type.
        db.rename_column(u'slides_slide', 'talk', 'talk_id')
        # Changing field 'Slide.talk'
        db.alter_column(u'slides_slide', 'talk_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['slides.Talk']))
        # Adding index on 'Slide', fields ['talk']
        db.create_index(u'slides_slide', ['talk_id'])


    def backwards(self, orm):
        # Removing index on 'Slide', fields ['talk']
        db.delete_index(u'slides_slide', ['talk_id'])

        # Deleting model 'Talk'
        db.delete_table(u'slides_talk')


        # Renaming column for 'Slide.talk' to match new field type.
        db.rename_column(u'slides_slide', 'talk_id', 'talk')
        # Changing field 'Slide.talk'
        db.alter_column(u'slides_slide', 'talk', self.gf('django.db.models.fields.CharField')(max_length=32))

    models = {
        u'slides.slide': {
            'Meta': {'object_name': 'Slide'},
            'colour_scheme': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'talk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['slides.Talk']", 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'time': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
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