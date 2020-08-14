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
    """ Search in food portions. Queryset: user=request.user or is public=True"""
    model = models.FoodPortion
    serializer_class = serializers.FoodPortionDetailSerializer
    filterset_class = filtersets.FoodPortionFilterSet


class SearchFoodCategoryViewSet(SearchBaseViewSet):
    """ Search in food categories. Queryset: user=request.user or is public=True"""
    model = models.FoodCategory
    serializer_class = serializers.FoodCategoryDetailSerializer
    filterset_class = filtersets.FoodCategoryFilterSet


class SearchFoodViewSet(SearchBaseViewSet):
    """ Search in foods. Queryset: user=request.user or is public=True"""
    model = models.Food
    serializer_class = serializers.FoodDetailSerializer
    filterset_class = filtersets.FoodFilterSet


class SearchActivityCategoryViewSet(SearchBaseViewSet):
    """ Search in activity categories. Queryset: user=request.user or is public=True"""
    model = models.ActivityCategory
    serializer_class = serializers.ActivityCategoryDetailSerializer
    filterset_class = filtersets.ActivityCategoryFilterSet


class SearchActivityViewSet(SearchBaseViewSet):
    """ Search in activities. Queryset: user=request.user or is public=True"""
    model = models.Activity
    serializer_class = serializers.ActivityDetailSerializer
    filterset_class = filtersets.ActivityFilterSet


class SearchFoodJournalViewSet(SearchBaseViewSet):
    """ Search in food journal. Queryset: user=request.user """
    model = models.FoodJournal
    serializer_class = serializers.FoodJournalDetailSerializer
    filterset_class = filtersets.FoodJournalFilterSet

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class SearchActivityJournalViewSet(SearchBaseViewSet):
    """ Search in activity journal. Queryset: user=request.user """
    model = models.ActivityJournal
    serializer_class = serializers.ActivityJournalDetailSerializer
    filterset_class = filtersets.ActivityJournalFilterSet

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
