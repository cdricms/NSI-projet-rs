"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from datetime import timedelta

from pathlib import Path

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = Path(BASE_DIR).resolve().parent


env_path=PROJECT_DIR/".env"
load_dotenv(dotenv_path=env_path)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# TODO: This key:
SECRET_KEY = 'django-insecure-=y(d)6_kx7gyg+ez94211plhhk_tzfn*vp)%i&56xcnky4rujc'
# with:
# SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# TODO: CHange this value:
DEBUG = True
# with:
# DEBUG = bool(os.getenv("DEBUG"))

ALLOWED_HOSTS = ["localhost"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'apirs',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'build/'),
        ],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': os.getenv("MONGO_DB"),
        'CLIENT': {
            'host': '127.0.0.1',
            'port': 27017,
            'username': os.getenv("MONGO_USERNAME"),
            'password': os.getenv("MONGO_PASSWORD"),
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

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTIFICATION_CLASSES": [
        "rest_framework_simplejwt.authentification.JWTAuthentification"
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,

}

if not DEBUG:

    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
            'rest_framework.renderers.JSONRenderer',
            # 'rest_framework.renderers.BrowsableAPIRenderer',
        ]
    

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ["JWT"],
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
}


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/assets/'
MEDIA_ROOT = BASE_DIR / 'static/media'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'build/assets'),
]

# Comment this when in production
CORS_ORIGIN_ALLOW_ALL = True

# And use this instead, with the proper urls.
# CORS_ALLOWED_ORIGINS = []
CSRF_TRUSTED_ORIGINS = ['http://localhost:3000']

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_PROFILE_MODULE = 'apirs.User'
AUTH_USER_MODEL = 'apirs.User'