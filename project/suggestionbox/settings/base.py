"""Settings shared by all deployments of suggestion box."""

import os


##############################################################################################
# Directories

SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.abspath(SETTINGS_DIR + "/../..")
GIT_DIR = os.path.abspath(PROJECT_DIR + "/..")


##############################################################################################
# Core Settings

# We keep our template files in the project "template" directory.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

INSTALLED_APPS = [
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'suggestions',
    'bootstrap3'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'suggestionbox.urls'

WSGI_APPLICATION = 'suggestionbox.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True
USE_L10N = True
USE_TZ = True


##############################################################################################
# Static Files
#
# This site doesn't do anything fancy for media/static--they're just kept on
# the filesystem. If we deployed at a PaaS place, we'd want to move to S3.

# Where we want to store static files.
STATIC_ROOT = GIT_DIR + "/static/"
STATIC_URL = "/static/"

# We keep our static source files in the "static" directory.
STATICFILES_DIRS = [os.path.join(PROJECT_DIR, "static")]


##############################################################################################
# Sessions
#
# We don't need any server-side storage of sessions, so just use cookies

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'


##############################################################################################
# Admin emails
#
# Email these people when errors happen on production sites

ADMINS = [('Joel', 'joel@joelburton.com'), ('Meggie', 'meggie@hackbrightacademy.com')]
SERVER_EMAIL = "joel@joelburton.com"
DEFAULT_FROM_EMAIL = 'joel@joelburton.com'


##############################################################################################
# Bootstrap / Bootstrap Admin

# Use Bootstrap for rendering admin fields
DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'

# 'required' html5 attribute does not play well with FF/Chrome and TinyMCE
BOOTSTRAP3 = {
    'set_required': False,
    'javascript_in_head': True,
    'set_placeholder': False,
}


##############################################################################################
# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'suggestionbox',
        'HOST': 'localhost',
    }
}


##############################################################################################
# Login / Users

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
