import json

from django.views import generic
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User

# Create your views here.
class UsernameValidationView(generic.View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data['username']
            if not str(username).isalnum():
                return JsonResponse(data={
                    'username_error' : 'Username should only contain alpha numeric characters'
                }, status=400)
            if User.objects.filter(username=username).exists():
                return JsonResponse(data={
                    'username_error' : 'This username is already taken. Please choose another name.'
                }, status=409)
            return JsonResponse(data={'Username is valid' : True}, status=200)
        except Exception as ex:
            print('USER NAME VALIDATION POST REQUEST ERROR: ', ex)

class RegistrationView(generic.View):
    template_name = 'authentication/register.html'

    def get(self, request):
        try:
            return render(request=request, template_name=self.template_name)
        except Exception as ex:
            print('REGISTER VIEW GET REQUEST ERROR: ', ex)