# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'UserProfile'
        db.create_table('logic_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('phoneNumber', self.gf('django.db.models.fields.CharField')(max_length=24)),
            ('dateModified', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('logic', ['UserProfile'])

        # Adding model 'Nursery'
        db.create_table('logic_nursery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('phoneNumber', self.gf('django.db.models.fields.CharField')(max_length=24)),
            ('dateCreated', self.gf('django.db.models.fields.DateTimeField')()),
            ('dateModified', self.gf('django.db.models.fields.DateTimeField')()),
            ('isActive', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('adminUser', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['logic.UserProfile'])),
        ))
        db.send_create_signal('logic', ['Nursery'])

        # Adding model 'Greenhouse'
        db.create_table('logic_greenhouse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('dateCreated', self.gf('django.db.models.fields.DateTimeField')()),
            ('dateModified', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('logic', ['Greenhouse'])

        # Adding model 'ScientificName'
        db.create_table('logic_scientificname', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal('logic', ['ScientificName'])

        # Adding model 'Plant'
        db.create_table('logic_plant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plantName', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('plantSize', self.gf('django.db.models.fields.FloatField')()),
            ('plantHeight', self.gf('django.db.models.fields.FloatField')()),
            ('plantType', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('plantImage', self.gf('django.db.models.fields.FilePathField')(max_length=100)),
            ('trunkDiameter', self.gf('django.db.models.fields.FloatField')()),
            ('variety', self.gf('django.db.models.fields.IntegerField')()),
            ('isAvailable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isBlooming', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('scientificName', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['logic.ScientificName'])),
            ('stock', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('dateCreated', self.gf('django.db.models.fields.DateTimeField')()),
            ('dateModified', self.gf('django.db.models.fields.DateTimeField')()),
            ('datePictureLastUpdated', self.gf('django.db.models.fields.DateTimeField')()),
            ('greenhouse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['logic.Greenhouse'])),
        ))
        db.send_create_signal('logic', ['Plant'])


    def backwards(self, orm):
        
        # Deleting model 'UserProfile'
        db.delete_table('logic_userprofile')

        # Deleting model 'Nursery'
        db.delete_table('logic_nursery')

        # Deleting model 'Greenhouse'
        db.delete_table('logic_greenhouse')

        # Deleting model 'ScientificName'
        db.delete_table('logic_scientificname')

        # Deleting model 'Plant'
        db.delete_table('logic_plant')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'logic.greenhouse': {
            'Meta': {'object_name': 'Greenhouse'},
            'dateCreated': ('django.db.models.fields.DateTimeField', [], {}),
            'dateModified': ('django.db.models.fields.DateTimeField', [], {}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'logic.nursery': {
            'Meta': {'object_name': 'Nursery'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'adminUser': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['logic.UserProfile']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'dateCreated': ('django.db.models.fields.DateTimeField', [], {}),
            'dateModified': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isActive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phoneNumber': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'logic.plant': {
            'Meta': {'object_name': 'Plant'},
            'dateCreated': ('django.db.models.fields.DateTimeField', [], {}),
            'dateModified': ('django.db.models.fields.DateTimeField', [], {}),
            'datePictureLastUpdated': ('django.db.models.fields.DateTimeField', [], {}),
            'greenhouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['logic.Greenhouse']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isAvailable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isBlooming': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'plantHeight': ('django.db.models.fields.FloatField', [], {}),
            'plantImage': ('django.db.models.fields.FilePathField', [], {'max_length': '100'}),
            'plantName': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'plantSize': ('django.db.models.fields.FloatField', [], {}),
            'plantType': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'scientificName': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['logic.ScientificName']"}),
            'stock': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'trunkDiameter': ('django.db.models.fields.FloatField', [], {}),
            'variety': ('django.db.models.fields.IntegerField', [], {})
        },
        'logic.scientificname': {
            'Meta': {'object_name': 'ScientificName'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'logic.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'dateModified': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phoneNumber': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['logic']
