"""
Django settings for Pizzo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/


# Import from local settings that aren't monitored by git
try:
    from local_settings import *
except ImportError:
    pass


# SECURITY WARNING: don't run with debug turned on in production!
# --- monitored by local_settings
# SECRET_KEY = ''


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# --- monitored by local_settings
# DATABASES = {
#     'default': {
#         'ENGINE': '',
#         'NAME': '',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',
#         'PORT': '',
#     }
# }


DEBUG = True

TEMPLATE_DEBUG = True


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'Templates').replace('\\','/'),
    #'/Templates'
    )

ALLOWED_HOSTS = []

# Application definition:
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'PizzoDB',
    # 'polls',
    # 'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Pizzo.urls'

WSGI_APPLICATION = 'Pizzo.wsgi.application'

SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
