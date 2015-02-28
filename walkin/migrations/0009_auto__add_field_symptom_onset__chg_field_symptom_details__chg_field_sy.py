# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Symptom.onset'
        db.add_column(u'walkin_symptom', 'onset',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Symptom.details'
        db.alter_column(u'walkin_symptom', 'details', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Symptom.duration'
        db.alter_column(u'walkin_symptom', 'duration', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):
        # Deleting field 'Symptom.onset'
        db.delete_column(u'walkin_symptom', 'onset')


        # Changing field 'Symptom.details'
        db.alter_column(u'walkin_symptom', 'details', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'Symptom.duration'
        db.alter_column(u'walkin_symptom', 'duration', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'opal.episode': {
            'Meta': {'object_name': 'Episode'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.CharField', [], {'default': "'inpatient'", 'max_length': '200'}),
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
        u'walkin.clinicalfindings': {
            'Meta': {'object_name': 'ClinicalFindings'},
            'abdominal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cardiovascular': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'dehydrated': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Episode']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jaundice': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'lymphadenopathy': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'lymphadenopathy_details': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'neurological': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'oropharnyx': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'other_findings': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
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
            'advice': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'date_of_appointment': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Episode']"}),
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
            'details': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Episode']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'onset': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'symptom_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Symptom']", 'null': 'True', 'blank': 'True'}),
            'symptom_ft': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'walkin.walkinnurseledcare': {
            'Meta': {'object_name': 'WalkinNurseLedCare'},
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Episode']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['walkin.Wi_nurse_reason']", 'null': 'True', 'blank': 'True'}),
            'reason_ft': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'treatment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'walkin.wi_nurse_reason': {
            'Meta': {'ordering': "['name']", 'object_name': 'Wi_nurse_reason'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['walkin']