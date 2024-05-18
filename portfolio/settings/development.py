import os
from .commons import *


SECRET_KEY = "django-insecure-9g(s@ntdxu%bl=z#l+2xx*8maaq^w%8vht2&uz+2!x6g^e)+0&"

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

SECURE_PROXY_SSL_HEADER = None

CSP_DEFAULT_SRC = False
CSP_STYLE_SRC = False
CSP_IMG_SRC = False
CSP_FONT_SRC = False
CSP_INCLUDE_NONCE_IN = [
    'script-src',
    'script-src-elem'
]


SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
SECURE_HSTS_SECONDS = None
SECURE_SSL_REDIRECT = False
SECURE_BROWSER_XSS_FILTER = False
SECURE_CONTENT_TYPE_NOSNIFF = False

