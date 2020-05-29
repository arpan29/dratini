"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mew.core.views import RUOK
from rest_framework_swagger.views import get_swagger_view

# from django.conf.urls.static import static

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('api/', include("webapp.apps.api.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', get_swagger_view(title='Microservice API')),
    path('ruok', RUOK.as_view(), name='ruok')
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
