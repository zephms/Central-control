"""qunkong1 URL Configuration

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
from first import views

urlpatterns = [
    path("", views.index, name="indexName"),
    path('admin/', admin.site.urls),
    path("register/", views.register, name="registerName"),
    path("login/", views.login, name="loginName"),
    path("verification/", views.verification, name="verificationName"),
    path("logout/", views.logout, name="logoutName"),
    path("centre/", views.centre, name="centreName"),
    path("addusr/", views.addusr, name="addusrName"),
    path("usr/", views.usr, name="usrName"),
    path("sendcmd/", views.sendcmd, name="sendcmdName"),

    path("imgAnalysis/", views.imgAnalysis, name="imgAnalysisName"),
    
    path("test/", views.test, name="testName"),
    path("testpost/", views.testpost, name="testpostName"),



]
