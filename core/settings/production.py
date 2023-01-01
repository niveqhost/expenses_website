from core.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['https://hai-expenses.up.railway.app']

# Origin checking failed - https://hai-expenses.up.railway.app does not match any trusted origins.
CSRF_TRUSTED_ORIGINS = ['https://hai-expenses.up.railway.app']
