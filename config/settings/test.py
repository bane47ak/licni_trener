"""Podešavanja za automatske testove."""

import tempfile

from .base import *  # noqa: F401,F403
from .base import STORAGES

DEBUG = False
ALLOWED_HOSTS = ["testserver", "localhost"]

# Emailovi u testovima ostaju u memoriji.
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
DEFAULT_FROM_EMAIL = "Lični trener <no-reply@localhost>"

# Brže heširanje lozinki u testovima.
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# Fajlovi iz testova idu u privremeni folder.
STORAGES = {
    **STORAGES,
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
        "OPTIONS": {"location": tempfile.mkdtemp(prefix="lt_test_"), "base_url": None},
    },
}
