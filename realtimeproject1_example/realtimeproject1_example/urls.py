"""realtimeproject1_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django .views.generic.base import TemplateView
from Hradmin import urls as admin
from manager import urls as manager
from Applicant_login import urls as Applicant
from Interviewer_Login import urls as Interview
from HRHead import urls as HR




urlpatterns = [

    path('index/',TemplateView.as_view(template_name="index.html"),name="index"),
    path('',include(admin)),
    path('',include(manager)),
    path('',include(Applicant)),
    path('',include(Interview)),
    path('',include(HR))
]
