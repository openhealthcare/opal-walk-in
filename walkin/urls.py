"""
Urls for the OPAL Walk In plugin
"""
from django.conf.urls import patterns, url

from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url('^templates/modals/discharge_walkin_episode.html/?$', TemplateView.as_view(template_name='discharge_walkin_episode.html')),
    url('^templates/modals/add_walkin_episode.html/?$', TemplateView.as_view(template_name='add_walkin_episode_modal.html')),
)
