"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""
import os

from django.core.asgi import get_asgi_application

from decouple import config
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', config('DJANGO_SETTINGS_MODULE'))

application = get_asgi_application()
