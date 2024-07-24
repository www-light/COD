from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.view import UserInfoViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    #path('api/', include(router.urls)),
]
