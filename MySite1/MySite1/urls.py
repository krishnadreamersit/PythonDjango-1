"""MySite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('app7', include('app7.urls')),
    path('app7_1', include('app7_1.urls')),
    path('app8_1/', include('app8_1.urls')),
    path('app8_2/', include('app8_2.urls')),
    path('app9_1/', include('app9_1.urls')),
    path('app10_1/', include('app10_1.urls')),
    path('app11_1', include('app11_1.urls')), # User Management
    path('app12_1/', include('app12_1.urls')), # Session
    path('app12_2/', include('app12_2.urls')), # Cookies
    path('app15_1/', include('app15_1.urls')), # Simple REST API
    path('app16_1/', include('app16_1.urls')), # File Upload
    path('app17_1/', include('app17_1.urls')), # Email Sending
    path('', include('app17_2.urls')), # Email Sending with Attachment
    path('admin/', admin.site.urls), # Admin Site
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)