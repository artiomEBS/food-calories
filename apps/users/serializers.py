from django.contrib.auth.models import User
from apps.users.models import Profile, Target
from rest_framework import serializers


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)
    target = TargetSerializer(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password', 'profile', 'target')
        extra_kwargs = {
            'username': {'required': True, 'allow_blank': False},
            'password': {'required': False, 'allow_blank': True, 'write_only': True},
        }


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)
        extra_kwargs = {
            'password': {'required': False, 'allow_blank': True, 'write_only': True},
        }
