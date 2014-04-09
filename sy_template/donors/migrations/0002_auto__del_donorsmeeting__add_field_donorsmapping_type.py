# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'DonorsMeeting'
        db.delete_table(u'donors_donorsmeeting')

        # Adding field 'DonorsMapping.type'
        db.add_column(u'donors_donorsmapping', 'type', self.gf('django.db.models.fields.CharField')(default='meeting', max_length=10), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'DonorsMeeting'
        db.create_table(u'donors_donorsmeeting', (
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keyword', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'donors', ['DonorsMeeting'])

        # Deleting field 'DonorsMapping.type'
        db.delete_column(u'donors_donorsmapping', 'type')


    models = {
        u'donors.donorsmapping': {
            'Meta': {'object_name': 'DonorsMapping'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['donors']
