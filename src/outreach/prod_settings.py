import os
from .settings import *  # noqa F403

DEBUG = False
DEBUG_TEMPLATE = False

SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = [".k12outreachboston.com"]

INSTALLED_APPS += [  # noqa F405
    'gunicorn',
]

DATABASES['default']['PASSWORD'] = os.environ['PG_PASS']  # noqa F405

static_dir = os.environ.get('STATIC_ROOT', None)
if static_dir is not None:
    STATIC_ROOT = static_dir

try:
    MIDDLEWARE.remove('querycount.middleware.QueryCountMiddleware')  # noqa F405
except ValueError:
    pass

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
