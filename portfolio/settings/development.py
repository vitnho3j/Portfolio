import os
from .commons import *
from csp.constants import SELF, NONCE, UNSAFE_HASHES, UNSAFE_INLINE


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

# CSP_DEFAULT_SRC = False
# CSP_STYLE_SRC = False
# CSP_IMG_SRC = False
# CSP_FONT_SRC = False
# CSP_INCLUDE_NONCE_IN = [
#     'script-src',
#     'script-src-elem'
# ]

# CSP_DEFAULT_SRC = ("'self'", "https://translate-pa.googleapis.com", "https://fonts.googleapis.com", "https://unpkg.com", "https://cdn.gtranslate.net", "https://www.gstatic.com", "https://translate.googleapis.com", "https://fonts.gstatic", "'unsafe-inline'")
# CSP_STYLE_SRC = ("'self'", "https://fonts.googleapis.com", "https://unpkg.com", "https://cdn.gtranslate.net", "'unsafe-inline'", "https://www.gstatic.com", "https://translate.googleapis.com", "https://fonts.gstatic.com")
# CSP_SCRIPT_SRC = ("'self'","https://translate-pa.googleapis.com", "https://cdn.gtranslate.net", "https://unpkg.com", "'unsafe-inline'", "https://translate.google.com", "https://www.gstatic.com", "https://translate.googleapis.com", "https://fonts.gstatic.com", "https://translate.google.com")
# CSP_IMG_SRC = ("'self'", "https://vddv-portfolio-storage.s3.amazonaws.com", "https://translate.google.com", "https://www.google.com", "https://translate-pa.googleapis.com", "https://fonts.googleapis.com", "https://unpkg.com", "https://cdn.gtranslate.net", "data:", "https://www.gstatic.com", "https://translate.googleapis.com", "https://fonts.gstatic.com", "'unsafe-inline'")
# CSP_FONT_SRC = ("'self'", "https://fonts.googleapis.com", "https://unpkg.com", "https://cdn.gtranslate.net", "https://www.gstatic.com", "https://translate.googleapis.com", "https://fonts.gstatic.com", "'unsafe-inline'")
# CSP_INCLUDE_NONCE_IN = [
#     'script-src',
#     'script-src-elem'
# ]

# CONTENT_SECURITY_POLICY = {
#     "DIRECTIVES":{
#         "defalt-src": [
#             SELF, 
#             "https://translate-pa.googleapis.com",
#             "https://fonts.googleapis.com", 
#             "https://unpkg.com", 
#             "https://unpkg.com/ionicons"
#             "https://cdn.gtranslate.net",
#             "https://www.gstatic.com", 
#             "https://translate.googleapis.com", 
#             "https://fonts.gstatic", 
#         ],
#         "connect-src": [
#             "https://unpkg.com"
#         ],
#         "script-src":[
#             SELF,
#             NONCE,
#             "https://translate-pa.googleapis.com", 
#             "https://cdn.gtranslate.net", 
#             "https://unpkg.com", 
#             "https://unpkg.com/ionicons", 
#             "https://translate.google.com", 
#             "https://www.gstatic.com", 
#             "https://translate.googleapis.com", 
#             "https://fonts.gstatic.com", 
#             "https://translate.google.com",
#         ],
#         "style-src":[
#             SELF,
#             NONCE,
#             "https://fonts.googleapis.com", 
#             "https://unpkg.com", 
#             "https://unpkg.com/ionicons",
#             "https://cdn.gtranslate.net",  
#             "https://www.gstatic.com", 
#             "https://translate.googleapis.com", 
#             "https://fonts.gstatic.com",
#         ],
#         "img-src":[
#             SELF,
#             "https://vddv-portfolio-storage.s3.amazonaws.com", 
#             "https://translate.google.com", 
#             "https://www.google.com", 
#             "https://translate-pa.googleapis.com", 
#             "https://fonts.googleapis.com", 
#             "https://unpkg.com", 
#             "https://unpkg.com/ionicons",
#             "https://cdn.gtranslate.net", 
#             "data:", 
#             "https://www.gstatic.com", 
#             "https://translate.googleapis.com", 
#             "https://fonts.gstatic.com", 
#         ],
#         "font-src":[
#             SELF,
#             "https://fonts.googleapis.com", 
#             "https://unpkg.com", 
#             "https://unpkg.com/ionicons",
#             "https://cdn.gtranslate.net", 
#             "https://www.gstatic.com", 
#             "https://translate.googleapis.com", 
#             "https://fonts.gstatic.com", 
#         ]
#     }
# }



CONTENT_SECURITY_POLICY = {
    "DIRECTIVES":{
        "default-src": [
            SELF,
            NONCE,
            UNSAFE_HASHES,
            "https://fonts.googleapis.com",
            "https://unpkg.com",
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
            "https://unpkg.com",
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
            "https://unpkg.com",
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
        ]
    }
}

SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
SECURE_HSTS_SECONDS = None
SECURE_SSL_REDIRECT = False
SECURE_BROWSER_XSS_FILTER = False
SECURE_CONTENT_TYPE_NOSNIFF = False

