# -*- coding: utf-8 -*-
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '../')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=r#xr(wfdh@*)a8omuulxg25&xhh2mpbla#0hb!1&*w5p7+8&)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Static asset configuration
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'social.apps.django_app.default',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'django.core.context_processors.request',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates/"),)

AUTHENTICATION_BACKENDS = (
    'social_auth.backend.RedditOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'social_auth.pipeline.set_token'
)

SOCIAL_AUTH_DISCONNECT_PIPELINE = (
    'social.pipeline.disconnect.get_entries',
    'social.pipeline.disconnect.revoke_tokens',
    'social.pipeline.disconnect.disconnect',
    'social_auth.pipeline.deauth_tagpro'
)

SOCIAL_AUTH_REDDIT_KEY = os.environ.get('SOCIAL_AUTH_REDDIT_KEY', None)
SOCIAL_AUTH_REDDIT_SECRET = os.environ.get('SOCIAL_AUTH_REDDIT_SECRET', None)

REDDIT_MOD_USERNAME = os.environ.get('REDDIT_MOD_USERNAME', None)
REDDIT_MOD_PASSWORD = os.environ.get('REDDIT_MOD_PASSWORD', None)
REDDIT_MOD_SUBREDDIT = os.environ.get('REDDIT_MOD_SUBREDDIT', None)


BOT_USER_AGENT = "/r/tagpro flair bot"

LOGIN_REDIRECT_URL = '/'

ROOT_URLCONF = 'tagpro_flair_bot.urls'

WSGI_APPLICATION = 'tagpro_flair_bot.wsgi.development.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

FLAIRS_BY_POSITION = {
    "-32px -16px": ("TagPro Developer", "Developer2"),
    "0px -16px": ("Community Contributor", "Contributor"),
    "-16px -16px": ("Level 1 Donor ($10)", "Donator"),
    "-48px -16px": ("Level 2 Donor ($40)", "Donator2"),
    "-64px -16px": ("Level 3 Donor ($100)", "Donator3"),
    "-80px -16px": ("Community Contest Winner", "Contest"),
    "-32px 0px": ("Monthly Leader Board Winner", "Monthly"),
    "-16px 0px": ("Weekly Leader Board Winner", "Weekly"),
    "0px 0px": ("Daily Leader Board Winner", "Daily"),
    "0px -32px": ("Happy Birthday TagPro", "Birthday"),
    "-16px -32px": ("Lucky You", "Lucky"),
    "-32px -32px": ("How Foolish", "Fools"),
    "-48px -32px": ("Hare Today, Goon Tomorrow", "Easter"),
    "0px -80px": ("Bacon (6°)", "Bacon"),
    "-16px -80px": ("Moon (11°)", "Moon"),
    "-32px -80px": ("Freezing (32°)", "Freezing"),
    "-48px -80px": ("Dolphin (42°)", "Dolphin"),
    "-64px -80px": ("Alien (51°)", "Alien"),
    "-80px -80px": ("Road Sign (66°)", "Route"),
    "-96px -80px": ("Peace (69°)", "Peace"),
    "-112px -80px": ("Microphone (98°)", "Microphone"),
    "-128px -80px": ("Boiling (100°)", "Boiling"),
    "-144px -80px": ("Bowling (300°)", "Bowling"),
    "-160px -80px": ("Pi (314°)", "Pi")
}

