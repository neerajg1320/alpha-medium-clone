from .base import * #noqa
from .base import env


SECRET_KEY = env(
    "DJANGO_SECRET_KEY", default="J5Ll1y-tXoINJtMGLToSN-WmLgqWnuyfW2J4ND1LFDqLPxpYcS0"
    )

DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

EMAIL_BACKEND = "djcelery_email.backend.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "support@apiimperfect.site"
DOMAIN = env("DOMAIN")

SITE_NAME="Medium Clone"
