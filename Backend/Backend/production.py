from .common import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
