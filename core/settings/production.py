from core.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['hai-expenses.up.railway.app']

# Origin checking failed - https://hai-expenses.up.railway.app does not match any trusted origins.
if not DEBUG:
    CSRF_TRUSTED_ORIGINS = ['hai-expenses.up.railway.app']
