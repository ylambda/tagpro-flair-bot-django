from functools import partial, wraps

from django import template
from django.conf import settings

register = template.Library()


def get_setting(setting_name):
    setting = getattr(settings, setting_name, '')
    return setting if setting is not None else ''


register.simple_tag(name='ga_tracking_id')(lambda: partial(get_setting, 'GOOGLE_ANALYTICS_TRACKING_ID')())
