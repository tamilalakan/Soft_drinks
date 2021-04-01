"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()

from account.views import (
	home,
    register,
    loginPage,
    logoutpage,
    forms,
    details,
    chart_view,
    addcompany,
    account,

	)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register', register, name='register'),
    path('login', loginPage, name='login'),
    path('logout', logoutpage, name='logout'),
    path('form',forms,name='forms'),
    path('detail/<str:id>',details,name='details'),
    path('chart_view/<str:id>',chart_view,name='chart_view'),
    path('addcompany/<str:id>',addcompany,name='addcompany'),
    path('account',account,name='account'),


]


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)