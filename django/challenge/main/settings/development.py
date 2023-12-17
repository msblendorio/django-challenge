from main.settings.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# Database

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'HOST': '_database',
#         'PORT': 5432,
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'NAME': 'challenge',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Mail

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
