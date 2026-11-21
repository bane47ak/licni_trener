"""Podešavanja za rad na tvom računaru (localhost)."""

from .base import *  # noqa: F401,F403
from .base import BASE_DIR

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Emailovi se ne šalju, nego se snimaju kao fajlovi u ovaj folder.
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = BASE_DIR / "lokalni_emailovi"
DEFAULT_FROM_EMAIL = "Lični trener <no-reply@localhost>"
