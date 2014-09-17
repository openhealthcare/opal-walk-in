"""
Urls for the OPAL observations plugin
"""
from django.conf.urls import patterns, url

from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url('^templates/modals/discharge_walkin_episode.html/?$', TemplateView.as_view(template_name='discharge_walkin_episode.html')),
)
