# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'DonorsMapping'
        db.create_table(u'donors_donorsmapping', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keyword', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'donors', ['DonorsMapping'])

        # Adding model 'DonorsMeeting'
        db.create_table(u'donors_donorsmeeting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keyword', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'donors', ['DonorsMeeting'])


    def backwards(self, orm):
        
        # Deleting model 'DonorsMapping'
        db.delete_table(u'donors_donorsmapping')

        # Deleting model 'DonorsMeeting'
        db.delete_table(u'donors_donorsmeeting')


    models = {
        u'donors.donorsmapping': {
            'Meta': {'object_name': 'DonorsMapping'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'donors.donorsmeeting': {
            'Meta': {'object_name': 'DonorsMeeting'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['donors']
