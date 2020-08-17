from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, Serializer
from apps.calorie_api import models


User = get_user_model()


# FoodPortion

class FoodPortionDetailSerializer(ModelSerializer):
    class Meta:
        model = models.FoodPortion
        exclude = ['user', 'is_public']


class FoodPortionCreateSerializer(ModelSerializer):
    class Meta:
        model = models.FoodPortion
        exclude = ['user', 'is_public', 'date_created', 'date_modified']


# FoodCategory

class FoodCategoryDetailSerializer(ModelSerializer):
    class Meta:
        model = models.FoodCategory
        exclude = ['user', 'is_public']


class FoodCategoryCreateSerializer(ModelSerializer):
    class Meta:
        model = models.FoodCategory
        exclude = ['user', 'is_public', 'date_created', 'date_modified']


# Food

class FoodDetailSerializer(ModelSerializer):
    category = FoodCategoryDetailSerializer(read_only=True)
    portions = FoodPortionDetailSerializer(many=True, read_only=True)

    class Meta:
        model = models.Food
        exclude = ['user', 'is_public']


class FoodCreateSerializer(ModelSerializer):
    class Meta:
        model = models.Food
        exclude = ['user', 'is_public', 'rating', 'date_created', 'date_modified']


# Activity

class ActivityDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Activity
        exclude = ['user', 'is_public']


class ActivityCreateSerializer(ModelSerializer):
    class Meta:
        model = models.Activity
        exclude = ['user', 'is_public', 'rating', 'date_created', 'date_modified']
