# -*- coding: utf-8 -*-

"""
Django settings for coccinella project.
"""

from django.utils.translation import ugettext_lazy as _
from cms_site.settings import *

# Application definition
INSTALLED_APPS = [
    'coccinella',
] + INSTALLED_APPS + [
    'photologue',
    'cmsplugin_photologue',
    'sortedm2m',
]

ROOT_URLCONF = 'coccinella.urls'

CMS_TEMPLATES = [
    ('default.html', _('Default')),
]

CMS_PLACEHOLDER_CONF = {
    'content': {
        'name': _('Content'),
    },
}

CMSPLUGIN_PHOTOLOGUE_PHOTO_TEMPLATES = (('coccinella', _('coccinella')),)
CMSPLUGIN_PHOTOLOGUE_GALLERY_TEMPLATES = (('coccinella', _('coccinella')),)
