from django.contrib.auth import get_user_model
from rest_framework.serializers import *
from apps.journal import models


User = get_user_model()


class FoodPortionDetailSerializer(ModelSerializer):
    class Meta:
        model = models.FoodPortion
        exclude = ['owner', 'is_public']


class FoodPortionCreateSerializer(ModelSerializer):
    class Meta:
        model = models.FoodPortion
        exclude = ['owner', 'is_public', 'date_created', 'date_modified']


class FoodCategoryDetailSerializer(ModelSerializer):
    portions = FoodPortionDetailSerializer(many=True, read_only=True)

    class Meta:
        model = models.FoodCategory
        exclude = ['owner', 'is_public']


class FoodCategoryCreateSerializer(ModelSerializer):
    class Meta:
        model = models.FoodCategory
        exclude = ['owner', 'is_public', 'date_created', 'date_modified']


class FoodDetailSerializer(ModelSerializer):
    category = FoodCategoryDetailSerializer(read_only=True)

    class Meta:
        model = models.Food
        exclude = ['owner', 'is_public']


class FoodCreateSerializer(ModelSerializer):
    class Meta:
        model = models.Food
        exclude = ['owner', 'is_public', 'rating', 'date_created', 'date_modified']


class ActivityCategoryDetailSerializer(ModelSerializer):
    class Meta:
        model = models.ActivityCategory
        exclude = ['owner', 'is_public']


class ActivityCategoryCreateSerializer(ModelSerializer):
    class Meta:
        model = models.ActivityCategory
        exclude = ['owner', 'is_public', 'date_created', 'date_modified']


class ActivityDetailSerializer(ModelSerializer):
    category = ActivityCategoryDetailSerializer(read_only=True)

    class Meta:
        model = models.ActivityCategory
        exclude = ['owner', 'is_public']


class ActivityCreateSerializer(ModelSerializer):
    class Meta:
        model = models.ActivityCategory
        exclude = ['owner', 'is_public', 'date_created', 'date_modified']


class FoodJournalDetailSerializer(ModelSerializer):
    food = FoodDetailSerializer(read_only=True)

    class Meta:
        model = models.ActivityCategory
        exclude = ['owner', 'is_public']


class FoodJournalCreateSerializer(ModelSerializer):
    class Meta:
        model = models.ActivityCategory
        exclude = ['owner', 'is_public', 'date_created', 'date_modified']


class ActivityJournalDetailSerializer(ModelSerializer):
    food = FoodDetailSerializer(read_only=True)

    class Meta:
        model = models.ActivityCategory
        exclude = ['owner', 'is_public']


class ActivityJournalCreateSerializer(ModelSerializer):
    class Meta:
        model = models.ActivityCategory
        exclude = ['owner', 'is_public', 'rating', 'date_created', 'date_modified']

