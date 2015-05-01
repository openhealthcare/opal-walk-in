"""
Standalone test runner for wardrounds plugin
"""
import os
import sys
from opal.core import application

class Application(application.OpalApplication):
    pass

from django.conf import settings

settings.configure(DEBUG=True,
                   DATABASES={
                       'default': {
                           'ENGINE': 'django.db.backends.sqlite3',
                       }
                   },
                   OPAL_OPTIONS_MODULE = 'walkin.tests.dummy_options_module',
                   ROOT_URLCONF='walkin.urls',
                   STATIC_URL='/assets/',
                   INSTALLED_APPS=('django.contrib.auth',
                                   'django.contrib.contenttypes',
                                   'django.contrib.sessions',
                                   'django.contrib.staticfiles',
                                   'django.contrib.admin',
                                   'opal',
                                   'walkin',))


from django.test.runner import DiscoverRunner
test_runner = DiscoverRunner(verbosity=1)
if len(sys.argv) == 2:
    failures = test_runner.run_tests([sys.argv[-1], ])
else:
    failures = test_runner.run_tests(['walkin', ])
if failures:
    sys.exit(failures)
