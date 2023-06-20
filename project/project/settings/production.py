from .base import *  # noqa
from .base import env

ADMINS = [("Neeraj Gupta", "neerajgupta.mbox@gmail.com")]

# ToDo: Add trusted production servers
CSRF_TRUSTED_ORIGINS = ["https://posprofile.com"]

user_email_accounts = {
    "neeraj": {
        "yahoo": {
            "host": "imap.mail.yahoo.com",
            "imap_port": 993,
            "smtp_address": "smtp.mail.yahoo.com",
            "smtp_port": 465,
            "username": "neeraj76",
            "password": 'feitecoaagdhxqcc',
            "email": "neeraj76@yahoo.com"
        },
        "gmail": {
            "host": "imap.gmail.com",
            "imap_port": 993,
            "smtp_address": "smtp.gmail.com",
            "smtp_port": 465,
            "username": "neerajgupta.finance",
            "password": 'chpdpemnebqfeoss',
            "email": "neerajgupta.finance@gmail.com"
        }
    }
}

SECRET_KEY = env("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["posprofile.com"])

ADMIN_URL = env("DJANGO_ADMIN_URL")

DATABASES = {"default": env.db("DATABASE_URL")}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

# TODO: change to 518400 later
SECURE_HSTS_SECONDS = 60

SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)

SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True
)

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL",
    default="Authors Haven Support <support@trainingwebdev.com>",
)

SITE_NAME = "Authors Haven"

SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)

EMAIL_SUBJECT_PREFIX = env(
    "DJANGO_EMAIL_SUBJECT_PREFIX",
    default="[Authors Haven]",
)

# EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
# EMAIL_HOST = "smtp.mailgun.org"
# EMAIL_HOST_USER = "postmaster@mg.trainingwebdev.com"
# EMAIL_HOST_PASSWORD = env("SMTP_MAILGUN_PASSWORD")
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# DOMAIN = env("DOMAIN")

"host": "imap.gmail.com",
"imap_port": 993,
"smtp_address": "smtp.gmail.com",
"smtp_port": 465,
"username": "neerajgupta.finance",
"password": 'chpdpemnebqfeoss',
"email": "neerajgupta.finance@gmail.com"

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = "imap.gmail.com"
EMAIL_HOST_USER = "neerajgupta.finance"
EMAIL_HOST_PASSWORD = "chpdpemnebqfeoss"
EMAIL_PORT = 465
EMAIL_USE_TLS = True

DOMAIN = env("DOMAIN")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
                      "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "handlers": ["console", "mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}
