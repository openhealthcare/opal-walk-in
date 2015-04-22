"""
Plugin definition
"""
from opal.core.plugins import OpalPlugin
from walkin import urls

class WalkinPlugin(OpalPlugin):
    urls = urls.urlpatterns
    javascripts = {
        'opal.controllers': [
            'js/walkin/controllers/walkin_hospital_number.js',
            'js/walkin/controllers/walkin_discharge.js'
        ]
    }
    actions = [
        'actions/walkin_next.html'
    ]
