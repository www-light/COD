from backend.models import UserInfo
from rest_framework import serializers


class ImageSerializer(serializers.Serializer):#定义一个序列化器
    image=serializers.ImageField()
