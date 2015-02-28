"""
Unit tests for the OPAL Walk in clinic plugin
"""
from django.test import TestCase
from mock import MagicMock

from opal.models import Episode

from walkin.models import Management

class ManagementTestCase(TestCase):
    "Tests the Walk-in Management record"
    
    def test_unicode(self):
        management = Management()
        self.assertEqual('Management: None', management.__unicode__())
