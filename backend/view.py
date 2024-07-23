from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from backend.models import UserInfo
from backend.serializer import UserInfoSerializer
from backend.filter import UserInfoFilter
from django_filters.rest_framework import DjangoFilterBackend


class UserInfoViewSet(ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    filter_class = UserInfoFilter
    filter_fields = ['username',]
    search_fields = ('username',)
