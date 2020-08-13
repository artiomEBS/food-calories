from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from apps.journal import models


User = get_user_model()


# FoodPortion

class FoodPortionDetailSerializer(ModelSerializer):
    class Meta:
        model = models.FoodPortion
        exclude = ['owner', 'is_public']


class FoodPortionCreateSerializer(ModelSerializer):
    class Meta:
        model = models.FoodPortion
        exclude = ['owner', 'is_public', 'date_created', 'date_modified']


# FoodCategory

class FoodCategoryDetailSerializer(ModelSerializer):
    class Meta:
        model = models.FoodCategory
        exclude = ['owner', 'is_public']


class FoodCategoryCreateSerializer(ModelSerializer):
    class Meta:
        model = models.FoodCategory
        exclude = ['owner', 'is_public', 'date_created', 'date_modified']


# Food

class FoodDetailSerializer(ModelSerializer):
    category = FoodCategoryDetailSerializer(read_only=True)
    portions = FoodPortionDetailSerializer(many=True, read_only=True)

    class Meta:
        model = models.Food
        exclude = ['owner', 'is_public']


class FoodCreateSerializer(ModelSerializer):
    class Meta:
        model = models.Food
        exclude = ['owner', 'is_public', 'rating', 'date_created', 'date_modified']


# FoodJournal

class FoodJournalDetailSerializer(ModelSerializer):
    food = FoodDetailSerializer(read_only=True)

    class Meta:
        model = models.FoodJournal
        exclude = ['owner']


class FoodJournalCreateSerializer(ModelSerializer):
    class Meta:
        model = models.FoodJournal
        exclude = ['owner', 'date_created', 'date_modified']


# ActivityCategory

class ActivityCategoryDetailSerializer(ModelSerializer):
    class Meta:
        model = models.ActivityCategory
        exclude = ['owner', 'is_public']


class ActivityCategoryCreateSerializer(ModelSerializer):
    class Meta:
        model = models.ActivityCategory
        exclude = ['owner', 'is_public', 'date_created', 'date_modified']


# Activity

class ActivityDetailSerializer(ModelSerializer):
    category = ActivityCategoryDetailSerializer(read_only=True)

    class Meta:
        model = models.Activity
        exclude = ['owner', 'is_public']


class ActivityCreateSerializer(ModelSerializer):
    class Meta:
        model = models.Activity
        exclude = ['owner', 'is_public', 'rating', 'date_created', 'date_modified']


# ActivityJournal

class ActivityJournalDetailSerializer(ModelSerializer):
    food = FoodDetailSerializer(read_only=True)

    class Meta:
        model = models.ActivityJournal
        exclude = ['owner']


class ActivityJournalCreateSerializer(ModelSerializer):
    class Meta:
        model = models.ActivityJournal
        exclude = ['owner', 'date_created', 'date_modified']
