from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

CACHE_BACKEND = getattr(settings, 'DBTEMPLATES_CACHE_BACKEND', None)

ADD_DEFAULT_SITE = getattr(settings, 'DBTEMPLATES_ADD_DEFAULT_SITE', True)

MEDIA_PREFIX = getattr(settings, 'DBTEMPLATES_MEDIA_PREFIX', None)

USE_REVERSION = getattr(settings, 'DBTEMPLATES_USE_REVERSION', False)

if USE_REVERSION and 'reversion'not in settings.INSTALLED_APPS:
    raise ImproperlyConfigured("Please add reversion to your INSTALLED_APPS setting to make use of it in dbtemplates.")

USE_CODEMIRROR = getattr(settings, 'DBTEMPLATES_USE_CODEMIRROR', False)
