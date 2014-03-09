import os
from presentation.settings.base import *


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!0gxy*sve7li-@z^5hca0a_e8)x6c-je4k#+i27po+^pur28k3'

STATIC_ROOT = os.path.join(os.getcwd(), "static/public")

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), "../../../shower"),
    os.path.join(os.path.dirname(__file__), "../../../static"),
)
