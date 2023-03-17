"""
Django settings for LinkedIn_Clone project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
import cloudinary_storage
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xjhvsilc1tp8n^_l1h_$bms&mpz%&ob2)e=6=*l4vj+3--9a+q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# setting the path for uploading images and videos in post model.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# for cloudinary storage
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://localhost:3001',
    'http://localhost:19006',
    'https://ditto-linkedin.herokuapp.com',
    'http://ditto-linkedin.herokuapp.com'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    #for image storage on cloudinary
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'rest_framework',
    # for authentication
    'rest_framework.authtoken',
    # for allow react to work with django rest framework
    'corsheaders',
    # our apps
    'UserApp',
    'PostApp',
    'ProfileApp'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LinkedIn_Clone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

AUTH_USER_MODEL = 'UserApp.User'

WSGI_APPLICATION = 'LinkedIn_Clone.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication'
    ]
}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# Local db config
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'linkedindb',
#         'USER': 'postgres',
#         'PASSWORD': os.environ.get('db_pwd'),
#         'HOST': '127.0.0.1',
#     }
# }

#Hekou database config
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'darbt3oa5uom0e',
#         'USER': 'pyahqwjpallcdp',
#         'PASSWORD': '3248d0096c43dfa0d9f07ff7333809ce6a82b83044f587cb65484f0011398ba4',
#         'HOST': 'ec2-34-206-8-52.compute-1.amazonaws.com',
#         'PORT': '5432',
#     },
# }






db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# credentials for CLOUDINARY_STORAGE
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'mindflowingblog',
    'API_KEY': '567811753678262',
    'API_SECRET': '1ekQ3qVaUyaWI4GJ6ifotljGVJo'
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# activate heroku settings for djnago
# django_on_heroku.settings(locals())
