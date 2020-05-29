from django.urls import path

from . import views

urlpatterns = [
    # Create Folder/ Get all folders
    path('v1/test', views.MyView.as_view(), name='test'),
]
