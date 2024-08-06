from .commons import *
from csp.constants import SELF, NONCE, UNSAFE_HASHES

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = False
ALLOWED_HOSTS = ['https://portifolio-site.fly.dev', 'www.portifolio-site.fly.dev', 'portifolio-site.fly.dev', 'vitordanieldeveloper.com', 'www.vitordanieldeveloper.com', 'https://www.vitordanieldeveloper.com', 'https://vitordanieldeveloper.com']

DATABASES = {
    "default": env.dj_db_url("DATABASE_URL", default="sqlite:///db.sqlite3"),
}

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'data/media'

CSRF_TRUSTED_ORIGINS = ['https://portifolio-site.fly.dev', 'https://vitordanieldeveloper.com']

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CONTENT_SECURITY_POLICY = {
    "DIRECTIVES":{
        "default-src": [
            SELF,
            NONCE,
            UNSAFE_HASHES,
            "https://fonts.googleapis.com",
            "https://cdn.gtranslate.net",
            "'sha256-uTMR0myRPuS/CaY9Wwm9o/PloGR0On61SBQgXRUlZog='"
        ],
        "style-src":[
            SELF,
            NONCE,
            UNSAFE_HASHES,
            "'sha256-uTMR0myRPuS/CaY9Wwm9o/PloGR0On61SBQgXRUlZog='",
            "'sha256-tTgjrFAQDNcRW/9ebtwfDewCTgZMFnKpGa9tcHFyvcs='",
            "'sha256-aqNNdDLnnrDOnTNdkJpYlAxKVJtLt9CtFLklmInuUAE='",
            "'sha256-YcAFp/goa4oZ/go0L/bJqARj1OFlyN88mkdtnxxdwqY='",
            "'sha256-65mkwZPt4V1miqNM9CcVYkrpnlQigG9H6Vi9OM/JCgY='",
            "'sha256-2Ohx/ATsoWMOlFyvs2k+OujvqXKOHaLKZnHMV8PRbIc='",
            "'sha256-PYJPy/i8uUXcvkFF68DWnALx/J1N5ddtrcRgEmORra8='",
            "'sha256-Johd5Ih43fYn+gVlcl7EGWAfQnsT/3vIvaiKxHXXHgc='",
            "'sha256-FICANCZamj/DX3lvcVNNj99LzpLFKnTI/DkvPLngmZU='",
            "'sha256-B6LEPigs3viM+y/BwYQU665laXgIDFgp+sr+sdoaJqQ='",
        ],
        "style-src-elem":[
            NONCE,
            SELF,
            "https://fonts.googleapis.com",
            "'sha256-NBfyYgxoWTkJ9SyHWLNVIq8UkKGvsaGPAaGmNMpVMSA='",
            "'sha256-Lcdm+l3ofbPMAFVaD9osqlF66mM1984Xamtc7xzQG44='",
            "https://www.gstatic.com",
        ],
        "script-src-elem":[
            SELF,
            NONCE,
            "https://cdn.gtranslate.net",
            "https://translate.google.com",
            "https://translate.googleapis.com",
            "'sha256-9G+2o+fiD9dlp1RUbKZfhCZNKjLJ8g+2PPLai/Se3nw='",
            "https://translate-pa.googleapis.com",
        ],
        "script-src":[
            SELF,
            NONCE,
            UNSAFE_HASHES,
            "'sha256-XM0dkxxQ/yTyBTwandCPlL7tDVunt/MZffFeWWfHKgg='",
            "'sha256-IPAXGUUOlmhnpLTjynKMcEDaJ2YoYgf3u/0mKujv9Tw='"
        ],
        "font-src":[
            SELF,
            "https://fonts.gstatic.com"
        ],
        "connect-src":[
            SELF,
            "https://translate.googleapis.com",
            "https://translate-pa.googleapis.com",
        ],
        "img-src":[
            SELF,
            "cdn.gtranslate.net",
            "https://fonts.gstatic.com",
            "https://www.gstatic.com",
            "https://www.google.com",
            "https://translate.googleapis.com",
            "http://translate.google.com",
            "data:",
            "vddv-portfolio-storage.s3.amazonaws.com",
        ]
    }
}
CSP_INCLUDE_NONCE_IN = [
    'script-src',
    'script-src-elem',
    'style-src'
]


SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 31536000 
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_FILE_OVERWRITE = False
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")


