# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Symptom'
        db.create_table(u'walkin_symptom', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('consistency_token', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('episode', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opal.Episode'], null=True)),
            ('details', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('duration_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opal.Duration'], null=True, blank=True)),
            ('duration_ft', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
            ('symptom_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opal.Symptom'], null=True, blank=True)),
            ('symptom_ft', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'walkin', ['Symptom'])

        # Adding model 'Findings_rash_type'
        db.create_table(u'walkin_findings_rash_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'walkin', ['Findings_rash_type'])

        # Adding model 'Findings_rash_distribution'
        db.create_table(u'walkin_findings_rash_distribution', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'walkin', ['Findings_rash_distribution'])

        # Adding model 'ClinicalFinding'
        db.create_table(u'walkin_clinicalfinding', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('consistency_token', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('episode', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opal.Episode'], null=True)),
            ('cervical_lymphadenopathy', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('inguinal_lymphadenopathy', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('jaundice', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('dehydrated', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('rash', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('cardiovascular', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('respiratory', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('abdominal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('oropharnyx', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('neurological', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('rash_type_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['walkin.Findings_rash_type'], null=True, blank=True)),
            ('rash_type_ft', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
            ('rash_distribution_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['walkin.Findings_rash_distribution'], null=True, blank=True)),
            ('rash_distribution_ft', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'walkin', ['ClinicalFinding'])

        # Adding model 'Walkin_hiv_declined_reason'
        db.create_table(u'walkin_walkin_hiv_declined_reason', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'walkin', ['Walkin_hiv_declined_reason'])

        # Adding model 'WalkinTest'
        db.create_table(u'walkin_walkintest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('consistency_token', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('episode', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opal.Episode'], null=True)),
            ('hiv_test', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('stool_ocp', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('malaria_film', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('hiv_declined_reason_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['walkin.Walkin_hiv_declined_reason'], null=True, blank=True)),
            ('hiv_declined_reason_ft', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'walkin', ['WalkinTest'])

        # Adding model 'Management_follow_up'
        db.create_table(u'walkin_management_follow_up', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'walkin', ['Management_follow_up'])

        # Adding model 'Management_clinics'
        db.create_table(u'walkin_management_clinics', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'walkin', ['Management_clinics'])

        # Adding model 'Management'
        db.create_table(u'walkin_management', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('consistency_token', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('episode', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opal.Episode'], null=True)),
            ('date_of_appointment', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('follow_up_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['walkin.Management_follow_up'], null=True, blank=True)),
            ('follow_up_ft', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
            ('follow_up_clinic_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['walkin.Management_clinics'], null=True, blank=True)),
            ('follow_up_clinic_ft', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'walkin', ['Management'])

    def backwards(self, orm):
        # Deleting model 'Symptom'
        db.delete_table(u'walkin_symptom')

        # Deleting model 'Findings_rash_type'
        db.delete_table(u'walkin_findings_rash_type')

        # Deleting model 'Findings_rash_distribution'
        db.delete_table(u'walkin_findings_rash_distribution')

        # Deleting model 'ClinicalFinding'
        db.delete_table(u'walkin_clinicalfinding')

        # Deleting model 'Walkin_hiv_declined_reason'
        db.delete_table(u'walkin_walkin_hiv_declined_reason')

        # Deleting model 'WalkinTest'
        db.delete_table(u'walkin_walkintest')

        # Deleting model 'Management_follow_up'
        db.delete_table(u'walkin_management_follow_up')

        # Deleting model 'Management_clinics'
        db.delete_table(u'walkin_management_clinics')

        # Deleting model 'Management'
        db.delete_table(u'walkin_management')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'opal.duration': {
            'Meta': {'ordering': "['name']", 'object_name': 'Duration'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'opal.episode': {
            'Meta': {'object_name': 'Episode'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'date_of_admission': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'discharge_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Patient']"})
        },
        u'opal.patient': {
            'Meta': {'object_name': 'Patient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'opal.symptom': {
            'Meta': {'ordering': "['name']", 'object_name': 'Symptom'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'opal.synonym': {
            'Meta': {'unique_together': "(('name', 'content_type'),)", 'object_name': 'Synonym'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'walkin.clinicalfinding': {
            'Meta': {'object_name': 'ClinicalFinding'},
            'abdominal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cardiovascular': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cervical_lymphadenopathy': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'dehydrated': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Episode']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inguinal_lymphadenopathy': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'jaundice': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'neurological': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'oropharnyx': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'rash': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'rash_distribution_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['walkin.Findings_rash_distribution']", 'null': 'True', 'blank': 'True'}),
            'rash_distribution_ft': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'rash_type_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['walkin.Findings_rash_type']", 'null': 'True', 'blank': 'True'}),
            'rash_type_ft': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'respiratory': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'walkin.findings_rash_distribution': {
            'Meta': {'ordering': "['name']", 'object_name': 'Findings_rash_distribution'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'walkin.findings_rash_type': {
            'Meta': {'ordering': "['name']", 'object_name': 'Findings_rash_type'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'walkin.management': {
            'Meta': {'object_name': 'Management'},
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'date_of_appointment': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Episode']", 'null': 'True'}),
            'follow_up_clinic_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['walkin.Management_clinics']", 'null': 'True', 'blank': 'True'}),
            'follow_up_clinic_ft': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'follow_up_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['walkin.Management_follow_up']", 'null': 'True', 'blank': 'True'}),
            'follow_up_ft': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'walkin.management_clinics': {
            'Meta': {'ordering': "['name']", 'object_name': 'Management_clinics'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'walkin.management_follow_up': {
            'Meta': {'ordering': "['name']", 'object_name': 'Management_follow_up'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'walkin.symptom': {
            'Meta': {'object_name': 'Symptom'},
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'duration_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Duration']", 'null': 'True', 'blank': 'True'}),
            'duration_ft': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Episode']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'symptom_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Symptom']", 'null': 'True', 'blank': 'True'}),
            'symptom_ft': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'walkin.walkin_hiv_declined_reason': {
            'Meta': {'ordering': "['name']", 'object_name': 'Walkin_hiv_declined_reason'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'walkin.walkintest': {
            'Meta': {'object_name': 'WalkinTest'},
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Episode']", 'null': 'True'}),
            'hiv_declined_reason_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['walkin.Walkin_hiv_declined_reason']", 'null': 'True', 'blank': 'True'}),
            'hiv_declined_reason_ft': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'hiv_test': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'malaria_film': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'stool_ocp': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['walkin']
