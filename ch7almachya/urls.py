"""
URL configuration for ch7almachya project.

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
from django.urls import path, include, re_path
from . import views
from . import settings
from django.conf.urls.static import static
from .files_render import firebase_messaging_sw
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('firebase-messaging-sw.js', firebase_messaging_sw),
    path('resized-image/<int:width>/', views.serve_resized_image, name='serve_resized_image'),
    path('api/set-language/', views.setLanguage),
    path('api/home/', views.home),
    path('api/get-ads/', views.get_ads),
    path('api/send-verification-token/', views.send_verfication_token),
    path("api/reset-password-validation/",views.reset_password_validation , name='reset-password-validation'),
    path('api/report/', views.report),
    path('api/user/', include('user.urls')),
    path('api/article/', include('article.urls')),
    path('api/dashboard/', include('dashboard.urls')),
    path('api/settings/', include('settings.urls')),
    path('api/others/', include('others.urls')),
    path('api/messaging/', include('messaging.urls')),
    path('api/checkUsername/', views.checkUsername),
    path('api/parameters/', views.parameters),
    path('api/contact-us/', views.contact_us),
    path('admin/', admin.site.urls),
    path('staff/', TemplateView.as_view(template_name='staff/index.html')),
    path('staff/<path:extra>/', TemplateView.as_view(template_name='staff/index.html')),
    path('api/staff/', include('staff.urls')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'^.*$', TemplateView.as_view(template_name='users/index.html')),
]