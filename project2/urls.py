"""
URL configuration for project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home),
    path('store/',Store),
    path('store/category/<cat_name>/<product_id>',ProductDetail),
    path('store/category/<x>',Category),
    path('store/add-to-cart/<product_id>',AddCart),
    path('cart/',Carts),
    path('store/remove-cart-item/<cart_id>',RemoveCart),
    path('store/remove/<product_id>',RemoveCartItem),
    path('register',Register),
    path('accounts/activate/<uid>/<token>',Activate),
    path('login',Login),
    path('logout',Logout),
    path('forgot-password',ForgotPassword),
    path('reset-password/<uid>/<token>',ResetPassword),
    path('reset-form-submit',ResetSubmit),
    path('checkout',checkout)


]+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
 
