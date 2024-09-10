from django.urls import path, include
from . import views

urlpatterns = [
    path('upload_images', views.upload_images.as_view()),
]