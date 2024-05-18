from .commons import *

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

CSP_DEFAULT_SRC = ("'self'", "https://translate-pa.googleapis.com", "https://fonts.googleapis.com", "https://unpkg.com", "https://cdn.gtranslate.net", "https://www.gstatic.com", "https://translate.googleapis.com", "https://fonts.gstatic", "'unsafe-inline'")
CSP_STYLE_SRC = ("'self'", "https://fonts.googleapis.com", "https://unpkg.com", "https://cdn.gtranslate.net", "'unsafe-inline'", "https://www.gstatic.com", "https://translate.googleapis.com", "https://fonts.gstatic.com")
CSP_SCRIPT_SRC = ("'self'","https://translate-pa.googleapis.com", "https://cdn.gtranslate.net", "https://unpkg.com", "'unsafe-inline'", "https://translate.google.com", "https://www.gstatic.com", "https://translate.googleapis.com", "https://fonts.gstatic.com", "https://translate.google.com")
CSP_IMG_SRC = ("'self'", "https://vddv-portfolio-storage.s3.amazonaws.com", "https://translate.google.com", "https://www.google.com", "https://translate-pa.googleapis.com", "https://fonts.googleapis.com", "https://unpkg.com", "https://cdn.gtranslate.net", "data:", "https://www.gstatic.com", "https://translate.googleapis.com", "https://fonts.gstatic.com", "'unsafe-inline'")
CSP_FONT_SRC = ("'self'", "https://fonts.googleapis.com", "https://unpkg.com", "https://cdn.gtranslate.net", "https://www.gstatic.com", "https://translate.googleapis.com", "https://fonts.gstatic.com", "'unsafe-inline'")
CSP_INCLUDE_NONCE_IN = [
    'script-src',
    'script-src-elem'
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


