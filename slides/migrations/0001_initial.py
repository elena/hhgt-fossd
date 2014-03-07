# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slide'
        db.create_table(u'slides_slide', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('template', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('colour_scheme', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('talk', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('time', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'slides', ['Slide'])


    def backwards(self, orm):
        # Deleting model 'Slide'
        db.delete_table(u'slides_slide')


    models = {
        u'slides.slide': {
            'Meta': {'object_name': 'Slide'},
            'colour_scheme': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'talk': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'time': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['slides']