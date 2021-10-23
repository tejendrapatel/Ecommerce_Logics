"""jan_2020 URL Configuration

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
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('students/', studentpage, name='students'),
    path('teachers/', teacherpage, name='teachers'),
    path('details/<int:s_id>', detailspage, name='details'),
    path('teacherdetails/<int:t_id>', teacherdetails, name='tdetails'),
    path('delete_student/<int:s_id>', s_delete, name='s_delete'),
    path('user/', userpage, name='user'),
    path('login/', loginpage, name='login'),
    path('contact/', contactpage, name='contact'),
    path('signup/', s_sign_up,  name='s_signup'),
    path('edit_details/<int:s_id>',edit_student,  name='s_edit'),
    path('tsignup/', tsign_up,  name='t_signup'),
]
