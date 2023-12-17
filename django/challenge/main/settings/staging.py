# from django.challenge.main.settings.settings import *
from main.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'database',
        'PORT': 5432,
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'NAME': 'challenge',
    }
}


# Mail completare con le credenziali del proprio account

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yourserver.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your@email.com'
EMAIL_HOST_PASSWORD = 'yourpassword'
