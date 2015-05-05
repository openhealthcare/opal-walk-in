"""
Models for the OPAL observations plugin
"""
from django.db import models

from opal.models import EpisodeSubrecord, option_models
from opal.core.fields import ForeignKeyOrFreeText
from opal.core.lookuplists import lookup_list

FollowUpLookupList         = type(*lookup_list('management_follow_up', module=__name__))
ClinicLookupList           = type(*lookup_list('management_clinics', module=__name__))
NursingReasonLookupList    = type(*lookup_list('wi_nurse_reason', module=__name__))
RashTypeLookupList         = type(*lookup_list('findings_rash_type', module=__name__))
RashDistributionLookupList = type(*lookup_list('findings_rash_distribution', module=__name__))


class Symptom(EpisodeSubrecord):
    _title = 'Symptoms'
    _icon = 'fa fa-stethoscope'
    
    symptom  = ForeignKeyOrFreeText(option_models['symptom'])
    duration = models.CharField(max_length=255, blank=True, null=True)
    details  = models.CharField(max_length=255, blank=True, null=True)
    onset    = models.CharField(max_length=255, blank=True, null=True)


class ClinicalFindings(EpisodeSubrecord):
    _is_singleton = True
    _title        = 'Clinical Findings'
    _icon         = 'fa fa-stethoscope'

    lymphadenopathy         = models.CharField(max_length=20, blank=True, null=True)
    lymphadenopathy_details = models.CharField(max_length=255, blank=True, null=True)
    jaundice                = models.CharField(max_length=20, blank=True)
    dehydrated              = models.CharField(max_length=20, blank=True)

    rash                    = models.CharField(max_length=20, blank=True)
    rash_type               = ForeignKeyOrFreeText(RashTypeLookupList)
    rash_distribution       = ForeignKeyOrFreeText(RashDistributionLookupList)

    cardiovascular          = models.CharField(max_length=255, blank=True, null=True)
    respiratory             = models.CharField(max_length=255, blank=True, null=True)
    abdominal               = models.CharField(max_length=255, blank=True, null=True)
    oropharnyx              = models.CharField(max_length=255, blank=True, null=True)
    neurological            = models.CharField(max_length=255, blank=True, null=True)
    other_findings          = models.CharField(max_length=255, blank=True, null=True)


class Management(EpisodeSubrecord):
    _icon = 'fa fa-list-ol'

    follow_up           = ForeignKeyOrFreeText(FollowUpLookupList)
    follow_up_clinic    = ForeignKeyOrFreeText(ClinicLookupList)
    date_of_appointment = models.DateField(null=True, blank=True)
    advice              = models.CharField(max_length=255, blank=True, null=True)
    results_actioned    = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u'Management: {0}'.format(self.id)


class WalkinNurseLedCare(EpisodeSubrecord):
    _icon  = 'fa fa-user-md'
    _title = 'Nurse led care'
    
    reason    = ForeignKeyOrFreeText(NursingReasonLookupList)
    treatment = models.TextField(blank=True, null=True)

