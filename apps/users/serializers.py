from django.contrib.auth.models import User

from apps.users.models import Profile, Target
from rest_framework import serializers


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = '__all__'


class TargetPUTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = '__all__'
        extra_kwargs = {
            'id': {'required': False},
            'energy': {'required': False},
            'protein': {'required': False},
            'carbohydrate': {'required': False},
            'fat': {'required': False},
            'fiber': {'required': False},
            'salt': {'required': False},
            'sugar': {'required': False},
            'user': {'required': False},
        }


class SWAGGERTargetPUTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ('energy', 'protein', 'carbohydrate', 'fat', 'fiber', 'salt', 'sugar')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfilePUTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        extra_kwargs = {
            'id': {'required': False},
            'gender': {'required': False},
            'height': {'required': False},
            'weight': {'required': False},
            'date_of_birth': {'required': False},
            'user': {'required': False},
        }


class SWAGGERProfilePUTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('gender', 'height', 'height', 'weight', 'date_of_birth',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password',)
        extra_kwargs = {
            'username': {'required': True, 'allow_blank': False},
            'password': {'required': False, 'allow_blank': True, 'write_only': True},
        }


class UserPUTSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',)
        extra_kwargs = {
            'first_name': {'required': False, 'allow_blank': True},
            'last_name': {'required': False, 'allow_blank': True},
            'email': {'required': False, 'allow_blank': True},
            'username': {'required': False, 'allow_blank': True},
            'password': {'required': False, 'allow_blank': True, 'write_only': True},
        }


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)
        extra_kwargs = {
            'password': {'required': False, 'allow_blank': True, 'write_only': True},
        }


class UserRecoverSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=False)


class UserFullSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)
    target = TargetSerializer(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password', 'profile', 'target')
        extra_kwargs = {
            'username': {'required': True, 'allow_blank': False},
            'password': {'required': False, 'allow_blank': True, 'write_only': True},
        }
