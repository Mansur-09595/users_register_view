from rest_framework import serializers
from .models import CustomUser


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'phone',)


class UserSerializer(serializers.ModelSerializer): # new
    class Meta:
        model = CustomUser
        fields = ('id', 'username',)