"""ecommerce URL Configuration

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
from shopping.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',Home,name= 'home'),
    path('about/',About,name= 'about'),
    path('contact/',Contact,name= 'contact'),
    path('blog/',Blog,name= 'blog'),
    path('blog_single/',Blog_single,name= 'blog_single'),
    path('product_single/<int:pro_id>/',Product_single,name= 'product_single'),
    path('checkout/',Checkout,name= 'checkout'),
    path('category_detail/<int:cat_id>/',Category_detail,name= 'category_detail'),
    path('sub_detail/<int:sub_id>/',Sub_detail,name= 'sub_detail'),
    path('cart/',Cart,name= 'cart'),
    path('Login/',LOGIN,name='Login'),
    path('forgot/', Forgot, name='forgot'),
    path('signup', Signup, name='signup'),
    path('Logout/',LOGOUT,name='Logout'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
