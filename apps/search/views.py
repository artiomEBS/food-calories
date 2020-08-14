import itertools

from django.db.models import Q
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from apps.journal import models
from apps.journal import serializers
from apps.search import filtersets


class SearchBaseViewSet(ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    model = None
    serializer_class = None
    filterset_class = None

    def get_queryset(self):
        query = Q(is_public=True) | Q(user=self.request.user)
        return self.model.objects.filter(query)


class SearchFoodPortionViewSet(SearchBaseViewSet):
    model = models.FoodPortion
    serializer_class = serializers.FoodPortionDetailSerializer
    filterset_class = filtersets.FoodPortionFilterSet


class SearchFoodCategoryViewSet(SearchBaseViewSet):
    model = models.FoodCategory
    serializer_class = serializers.FoodCategoryDetailSerializer
    filterset_class = filtersets.FoodCategoryFilterSet


class SearchFoodViewSet(SearchBaseViewSet):
    model = models.Food
    serializer_class = serializers.FoodDetailSerializer
    filterset_class = filtersets.FoodFilterSet


class SearchActivityCategoryViewSet(SearchBaseViewSet):
    model = models.ActivityCategory
    serializer_class = serializers.ActivityCategoryDetailSerializer
    filterset_class = filtersets.ActivityCategoryFilterSet


class SearchActivityViewSet(SearchBaseViewSet):
    model = models.Activity
    serializer_class = serializers.ActivityDetailSerializer
    filterset_class = filtersets.ActivityFilterSet


class SearchJournalBaseViewSet(ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    model = None
    serializer_class = None
    filterset_class = None

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class SearchFoodJournalViewSet(SearchJournalBaseViewSet):
    model = models.FoodJournal
    serializer_class = serializers.FoodJournalDetailSerializer
    filterset_class = filtersets.FoodJournalFilterSet


class SearchActivityJournalViewSet(SearchJournalBaseViewSet):
    model = models.ActivityJournal
    serializer_class = serializers.ActivityJournalDetailSerializer
    filterset_class = filtersets.ActivityJournalFilterSet
