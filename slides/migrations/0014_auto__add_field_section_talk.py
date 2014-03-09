# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Section.talk'
        db.add_column(u'slides_section', 'talk',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['slides.Talk'], null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field version on 'Slide'
        db.delete_table(db.shorten_name(u'slides_slide_version'))


    def backwards(self, orm):
        # Deleting field 'Section.talk'
        db.delete_column(u'slides_section', 'talk_id')

        # Adding M2M table for field version on 'Slide'
        m2m_table_name = db.shorten_name(u'slides_slide_version')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('slide', models.ForeignKey(orm[u'slides.slide'], null=False)),
            ('version', models.ForeignKey(orm[u'slides.version'], null=False))
        ))
        db.create_unique(m2m_table_name, ['slide_id', 'version_id'])


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
            'versionA': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'versionB': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'versionC': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'slides.talk': {
            'Meta': {'object_name': 'Talk'},
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