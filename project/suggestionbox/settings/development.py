"""Development settings for suggestion-box project."""

from base import *
from django.core.mail.utils import DNS_NAME


# noinspection SpellCheckingInspection
SECRET_KEY = 'i^ari$22!b+&pwhm=o7h-%vr-%us)#k=q0!g9qcaz*a#!h!k*c'

DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += [
    'debug_toolbar',
]


##############################################################################################
# Email
#
# We don't want to send real email, so just print to the console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Fix for broken DNS at some wifi hot-spots
DNS_NAME._fqdn = "localhost"


##############################################################################################
# Logging & Error Reporting

# Blather on about every little thing that happens. We programmers get lonely.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'factory': {   # FactoryBoy is too chatty!
            'handlers': ['console'],
            'level': 'INFO',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        }

    },
}


##############################################################################################
# Caching --- don't actually cache

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


