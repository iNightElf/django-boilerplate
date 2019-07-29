from .base import *

DEBUG = False

ALLOWED_HOSTS = ['ip-adress', 'www.website.com']

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


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your dbname',
        'USER': 'your database user name',
        'PASSWORD': 'localhost',
        'PORT': ''
    }
}


STRIPE_PUBLIC_KEY = 'live-public-key'
STRIPE_SECRET_KEY = 'live-secret-key'
