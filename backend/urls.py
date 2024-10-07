from django.urls import path, include
from . import views
from . import views1

urlpatterns = [
    path('upload_images', views.upload_images.as_view()),
    path('random_animal', views1.get_random_animal, name='random_aninal'),
]