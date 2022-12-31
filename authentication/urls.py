from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from authentication.views import *

app_name = 'authentication'
urlpatterns = [
    path('register/', RegistrationView.as_view() , name='register'),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()) , name='validate-username'),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()) , name='validate-email'),
]
