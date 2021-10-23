
from django.contrib import admin
from django.urls import path
from blog.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',firstpage,name = "home"),
    path('contact/',secondpage,name = 'contact'),
    path('details/<int:c_id>/',Details,name='details'),
    path('detail/<int:v1>/<int:v2>/<str:v3>/',detail,name='detail'),
    path('Add_student/',add_student,name='add_student'),
]
