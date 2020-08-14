from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, Serializer

from apps.calorie_api.serializers import ActivityDetailSerializer, FoodDetailSerializer
from apps.journal import models


User = get_user_model()



# FoodJournal

class FoodJournalDetailSerializer(ModelSerializer):
    food = FoodDetailSerializer(read_only=True)

    class Meta:
        model = models.FoodJournal
        exclude = ['user']


class FoodJournalCreateSerializer(ModelSerializer):
    class Meta:
        model = models.FoodJournal
        exclude = ['user', 'date_created', 'date_modified']





# ActivityJournal

class ActivityJournalDetailSerializer(ModelSerializer):
    activity = ActivityDetailSerializer(read_only=True)

    class Meta:
        model = models.ActivityJournal
        exclude = ['user']


class ActivityJournalCreateSerializer(ModelSerializer):
    class Meta:
        model = models.ActivityJournal
        exclude = ['user', 'date_created', 'date_modified']


class JournalSerializer(Serializer):
    food_journal = FoodJournalDetailSerializer(many=True, read_only=True)
    activity_journal = ActivityJournalDetailSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        return None

    def create(self, validated_data):
        return None
