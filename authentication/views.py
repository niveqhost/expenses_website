import json

from django.views import generic
from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse
from validate_email import validate_email
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.template.loader import render_to_string

from authentication import models as auth_models

# Create your views here.
class UsernameValidationView(generic.View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data['username']
            if not str(username).isalnum():
                return JsonResponse(data={
                    'username_error' : 'Username should only contain alpha numeric characters.'
                }, status=400)
            if User.objects.filter(username=username).exists():
                return JsonResponse(data={
                    'username_error' : 'This username is already taken. Please choose another name.'
                }, status=409)
            return JsonResponse(data={'username_valid' : True}, status=200)
        except Exception as ex:
            print('USER NAME VALIDATION POST REQUEST ERROR: ', ex)

class EmailValidationView(generic.View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data['email']
            if not validate_email(email=email):
                return JsonResponse(data={
                    'email_error' : 'Email is invalid.'
                }, status=400)
            if User.objects.filter(email=email).exists():
                return JsonResponse(data={
                    'email_error' : 'This email is already taken. Please choose another email.'
                }, status=409)
            return JsonResponse(data={'email_valid' : True}, status=200)
        except Exception as ex:
            print('EMAIL VALIDATION POST REQUEST ERROR: ', ex)

class RegistrationView(generic.View):
    template_name = 'authentication/register.html'

    def get(self, request):
        try:
            return render(request=request, template_name=self.template_name)
        except Exception as ex:
            print('REGISTER VIEW GET REQUEST ERROR: ', ex)

    def post(self, request):
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            context = {
                'username': username,
                'email': email,
                'password': password
            }

            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already taken. Please choose another name.')
                return render(request, self.template_name, context)

            if User.objects.filter(email=email).exists():
                messages.error(request, 'This email is already taken. Please choose another email.')
                return render(request, self.template_name, context)

            if len(password) < 6:
                messages.error(request, 'Password must be more than 6 characters. Try another password.')
                return render(request, self.template_name, context)
            # Create user
            user = auth_models.CustomUser.objects.create(username=username, raw_password=password, email=email)
            user.save()
            # Send email
            email_subject = "Thử nghiệm tính năng gửi mail cho khách hàng."
            email_body = render_to_string('authentication/register_email.html', context)
            from_email = 'cskh@hotro.sbidu.vn'
            email_object = EmailMessage(
                email_subject,
                email_body,
                from_email,
                [email],
            )
            email_object.content_subtype = "html"
            email_object.send(fail_silently=False)
            messages.success(request, 'We sent you an email. Check your inbox.')
            return render(request, self.template_name)

        except Exception as ex:
            print('REGISTER VIEW POST REQUEST ERROR: ', ex)
