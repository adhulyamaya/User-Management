from __future__ import unicode_literals
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from six import text_type
from django.contrib.auth.models import User


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(UserTokenObtainPairSerializer, cls).get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username']

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.save()
        return user


class LogInSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=16)