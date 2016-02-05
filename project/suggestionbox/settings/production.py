"""Deployment settings for frodo project."""

from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['*']

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

##############################################################################################
# Database

# Use production PG database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('PG_DB', 'suggestionbox'),
        'HOST': os.environ.get('PG_HOST', 'localhost'),
        'PORT': os.environ.get('PG_PORT', 5432),
        'USER': os.environ.get('PG_USER', 'suggestionbox'),
        'PASSWORD': os.environ.get('PG_PASSWORD'),
        'CONN_MAX_AGE': None,
    }
}

##############################################################################################
# Logging & Error Reporting

# By default, we write reasonably important things (INFO and above) to the console
# We email admins on a site error or a security issue and also propagate
# this up to the Heroku logs.

LOGGING = {
    'disable_existing_loggers': False,
    'version': 1,

    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'WARNING',
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['console', 'mail_admins'],
            'level': 'WARNING',
            'propagate': True,
        },
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}

##############################################################################################
# Email
#
# We use AWS SES for sending email

EMAIL_HOST = "email-smtp.us-east-1.amazonaws.com"
# noinspection SpellCheckingInspection
EMAIL_HOST_USER = "AKIAIDQJEDLNTSM73G7A"
EMAIL_HOST_PASSWORD = os.environ.get('AWS_EMAIL_PASSWORD')
EMAIL_USE_TLS = True


##############################################################################################
# Caches
#

# Once we decide to turn caching on ...


##############################################################################################
# Template Loaders
#
# Performance improvement; template changes not effective until the process is restarted.

TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader',
     ('django.template.loaders.filesystem.Loader',
      'django.template.loaders.app_directories.Loader')
     )
]
del TEMPLATES[0]['APP_DIRS']


