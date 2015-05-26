"""
Models for the OPAL observations plugin
"""
from django.db import models

from opal import models as omodels
from opal.core import lookuplists
from opal.core.fields import ForeignKeyOrFreeText

class Management_follow_up(lookuplists.LookupList): pass
class Management_clinics(lookuplists.LookupList): pass
class Wi_nurse_reason(lookuplists.LookupList): pass
class Findings_rash_type(lookuplists.LookupList): pass
class Findings_rash_distribution(lookuplists.LookupList): pass

class Symptom(omodels.EpisodeSubrecord):
    _title = 'Symptoms'
    _icon = 'fa fa-stethoscope'
    
    symptom  = ForeignKeyOrFreeText(omodels.Symptom)
    duration = models.CharField(max_length=255, blank=True, null=True)
    details  = models.CharField(max_length=255, blank=True, null=True)
    onset    = models.CharField(max_length=255, blank=True, null=True)


class ClinicalFindings(omodels.EpisodeSubrecord):
    _is_singleton = True
    _title        = 'Clinical Findings'
    _icon         = 'fa fa-stethoscope'

    lymphadenopathy         = models.CharField(max_length=20, blank=True, null=True)
    lymphadenopathy_details = models.CharField(max_length=255, blank=True, null=True)
    jaundice                = models.CharField(max_length=20, blank=True)
    dehydrated              = models.CharField(max_length=20, blank=True)

    rash                    = models.CharField(max_length=20, blank=True)
    rash_type               = ForeignKeyOrFreeText(Findings_rash_type)
    rash_distribution       = ForeignKeyOrFreeText(Findings_rash_distribution)

    cardiovascular          = models.CharField(max_length=255, blank=True, null=True)
    respiratory             = models.CharField(max_length=255, blank=True, null=True)
    abdominal               = models.CharField(max_length=255, blank=True, null=True)
    oropharnyx              = models.CharField(max_length=255, blank=True, null=True)
    neurological            = models.CharField(max_length=255, blank=True, null=True)
    other_findings          = models.CharField(max_length=255, blank=True, null=True)


class Management(omodels.EpisodeSubrecord):
    _icon = 'fa fa-list-ol'

    follow_up           = ForeignKeyOrFreeText(Management_follow_up)
    follow_up_clinic    = ForeignKeyOrFreeText(Management_clinics)
    date_of_appointment = models.DateField(null=True, blank=True)
    advice              = models.CharField(max_length=255, blank=True, null=True)
    results_actioned    = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u'Management: {0}'.format(self.id)


class WalkinNurseLedCare(omodels.EpisodeSubrecord):
    _icon  = 'fa fa-user-md'
    _title = 'Nurse led care'
    
    reason    = ForeignKeyOrFreeText(Wi_nurse_reason)
    treatment = models.TextField(blank=True, null=True)

