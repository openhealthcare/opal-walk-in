"""
Models for the OPAL observations plugin
"""
from django.db import models

from opal.models import EpisodeSubrecord, option_models
from opal.utils.fields import ForeignKeyOrFreeText
from opal.utils.models import lookup_list


class Symptom(EpisodeSubrecord):
    _title = 'Symptoms'
    _fieldnames = [
        'episode_id',
        'symptom', 'duration',
        'details'
        ]
    symptom = ForeignKeyOrFreeText(option_models['symptom'])
    duration = ForeignKeyOrFreeText(option_models['duration'])
    details = models.CharField(max_length=255, blank=True)


RashTypeLookupList = type(*lookup_list('findings_rash_type', module=__name__))
RashDistributionLookupList = type(*lookup_list('findings_rash_distribution', module=__name__))

class ClinicalFinding(EpisodeSubrecord):
    _title = 'Clinical Findings'
    cervical_lymphadenopathy = models.CharField(max_length=20, blank=True)
    inguinal_lymphadenopathy = models.CharField(max_length=20, blank=True)
    jaundice = models.CharField(max_length=20, blank=True)
    dehydrated = models.CharField(max_length=20, blank=True)

    rash = models.CharField(max_length=20, blank=True)
    rash_type = ForeignKeyOrFreeText(RashTypeLookupList)
    rash_distribution = ForeignKeyOrFreeText(RashDistributionLookupList)

    cardiovascular = models.CharField(max_length=255, blank=True, null=True)
    respiratory = models.CharField(max_length=255, blank=True, null=True)
    abdominal = models.CharField(max_length=255, blank=True, null=True)
    oropharnyx = models.CharField(max_length=255, blank=True, null=True)
    neurological = models.CharField(max_length=255, blank=True, null=True)
    other_findings = models.CharField(max_length=255, blank=True, null=True)


FollowUpLookupList = type(*lookup_list('management_follow_up', module=__name__))
ClinicLookupList = type(*lookup_list('management_clinics', module=__name__))

class Management(EpisodeSubrecord):
    follow_up = ForeignKeyOrFreeText(FollowUpLookupList)
    follow_up_clinic = ForeignKeyOrFreeText(ClinicLookupList)
    date_of_appointment = models.DateField(null=True, blank=True)

