from django.urls import path

from . import views

urlpatterns = [
    # URLs
    path('v1/test', views.MyView.as_view(), name='test'),
]
