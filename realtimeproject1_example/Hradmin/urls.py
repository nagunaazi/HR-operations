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
from django.urls import path
from django .views.generic.base import TemplateView
from Hradmin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_login_page/',views.AdminLogin.as_view(),name="admin_login_page"),
    path('admin_home_page/',views.AdminHome.as_view(),name="admin_home_page"),
    path('add_employee_page/', views.AddEmployee.as_view(), name="add_employee_page"),
    path('view_employee_details/',views.ViewEmployeeDetails.as_view(),name="view_employee_details"),
    path('update/',views.UpdateEmployee.as_view(),name="update"),
    path('update_employee_details/',views.UpdateEmployeeDetails.as_view(),name="update_employee_details"),
    path('delete/',views.Delete.as_view(),name="delete"),



]
