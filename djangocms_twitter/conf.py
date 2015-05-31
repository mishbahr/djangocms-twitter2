# -*- coding: utf-8 -*-
from django.conf import settings  # noqa
from django.utils.translation import ugettext_lazy as _

from appconf import AppConf


class DjangoCMSTwitterConf(AppConf):
    PLUGIN_MODULE = _('Generic')
    PLUGIN_NAME = _('Twitter')

    PAGE_ONLY = False
    PARENT_CLASSES = None
    REQUIRE_PARENT = False
    TEXT_ENABLED = False
    DEFAULT_TEMPLATE = 'djangocms_twitter/default.html'

    TEMPLATES = (
        ('djangocms_twitter/default.html', _('Default')),
    )

    CACHE_DURATION = 300  # 5 mins

    class Meta:
        prefix = 'djangocms_twitter'
