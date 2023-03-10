"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('expenses.urls', namespace='expenses'), name='expenses_app'),
    path('account/', include('authentication.urls', namespace='authentication'), name='authentication_app'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) # Thu muc noi chua cac tep tin css, js, hinh anh
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Thu muc cho nguoi dung tai len cac hinh anh, am thanh, video,...
