"""
Plugin definition
"""
from opal.core.plugins import OpalPlugin

from walkin.urls import urlpatterns

class WalkinPlugin(OpalPlugin):
    urls = urlpatterns
    javascripts = {
        'opal.controllers': [
            'js/walkin/controllers/walkin_hospital_number.js',
            'js/walkin/controllers/walkin_discharge.js',
            'js/walkin/controllers/nurse_investigation.js'
        ]
    }
    actions = [
        'actions/walkin_next.html',
        'actions/nurse_investigations.html'
    ]
