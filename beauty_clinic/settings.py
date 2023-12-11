"""
Django settings for beauty_clinic project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path
import mimetypes
import django
from django.utils.encoding import force_str
django.utils.encoding.force_text = force_str
from dotenv import load_dotenv


load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))






# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cmf%aiq(sw8)t+f&h8zpyp_$f0!(jh@c!dw+1z@xk!339zs7dx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '10.0.2.2',
    '127.0.0.1',
    'beautyclinic.pythonanywhere.com',
    'beautyclinic22.pythonanywhere.com',
]


# Application definition

INSTALLED_APPS = [
    'notifications',
    'app',
    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'smart_selects',
    'rest_framework',
    'crispy_forms',
    'django_tables2',
    'crispy_bootstrap5',
    'django_bootstrap5',
]

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
    )
}

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'beauty_clinic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'app.context_processors.global_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'beauty_clinic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

if os.environ.get('DJANGO_ENV') == "LOCAL":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'beauty-clinic',
            'USER': 'root',
            'PASSWORD': 'admin',
            'HOST': 'localhost',
            'PORT': '3306',
            'OPTIONS': {
                    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            }
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'beautyclinic$default',
            'USER': 'beautyclinic',
            'PASSWORD': 'notCommonPassword123$',
            'HOST': 'beautyclinic.mysql.pythonanywhere-services.com',
            'PORT': '3306',
            'OPTIONS': {
                    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                    
                    
            }
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True

TIME_ZONE = 'Asia/Manila'

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Media Folder Setings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = "app.CustomUser"

SECURE_CROSS_ORIGIN_OPENER_POLICY = None
# JQUERY_URL = True
USE_DJANGO_JQUERY = True
mimetypes.add_type("text/javascript", ".js", True)

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
)

EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'login'  # this is the name of the url

LOGOUT_REDIRECT_URL = '/'


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"