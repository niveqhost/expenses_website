from django.urls import path
from expenses.views import *

app_name = 'expenses'
urlpatterns = [
    path('', IndexView.as_view() , name='home-page'),
]
