from base import *

DEBUG = False

import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')

WSGI_APPLICATION = 'tagpro_flair_bot.wsgi.heroku.application'

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

RAVEN_PUBLIC_KEY = os.environ.get('RAVEN_PUBLIC_KEY', None)
RAVEN_PRIVATE_KEY = os.environ.get('RAVEN_PRIVATE_KEY', None)
RAVEN_PROJECT_ID = os.environ.get('RAVEN_PROJECT_ID', None)

if RAVEN_PUBLIC_KEY and RAVEN_PRIVATE_KEY and RAVEN_PROJECT_ID:
    RAVEN_CONFIG = {
        'dsn': 'https://%s:%s@app.getsentry.com/%s' % (
            RAVEN_PUBLIC_KEY, RAVEN_PRIVATE_KEY, RAVEN_PROJECT_ID)}

    INSTALLED_APPS = INSTALLED_APPS + (
        'raven.contrib.django.raven_compat',)

try:
    from localsettings import *
except ImportError:
    pass
