from django.urls import path, include
from . import views
from . import views1
from.views3 import check_animal_name

app_name = 'backend'

urlpatterns = [
    path('upload_images', views.upload_images.as_view()),
    path('random_animal', views1.get_random_animal, name='random_aninal'), 
    path('check_animal_name/', check_animal_name, name='check_animal_name'),

]