# -*- coding: utf-8 -*-
import os

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

ADMINS = (('Adnane Belmadiaf', 'your-email@provider.com'),)
TIME_ZONE = 'Africa/Casablanca'

MANAGERS = (('Adnane Belmadiaf', 'your-email@provider.com'),)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'demo.db',
    }
}

TEMPLATE_DIRS = [os.path.join(PROJECT_PATH, "templates")]

SECRET_KEY = ''

DEBUG = True
TEMPLATE_DEBUG = DEBUG
STATIC_SERVE = True

SITE_ID = 1
SITE_URL = "http://127.0.0.1:8000"

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django_browserid',
    'demo',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_browserid.auth.BrowserIDBackend',
)

STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/media-admin/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

LOGIN_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL_FAILURE = '/'
LOGOUT_REDIRECT_URL = '/'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.debug',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'django_browserid.context_processors.browserid'
)

USE_ETAGS = True
USE_I18N = True
LANGUAGE_CODE = 'fr-fr'

BROWSERID_CREATE_USER = True
def username(email):
    return email.rsplit('@', 1)[0]
BROWSERID_USERNAME_ALGO = username
