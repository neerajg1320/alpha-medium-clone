from .base import * #noqa
from .base import env


SECRET_KEY = env(
    "DJANGO_SECRET_KEY", default="J5Ll1y-tXoINJtMGLToSN-WmLgqWnuyfW2J4ND1LFDqLPxpYcS0"
    )

DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]