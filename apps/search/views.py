from django.db.models import Q
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from apps.calorie_api.models import FoodPortion, FoodCategory, Food, Activity
from apps.calorie_api.serializers import FoodPortionDetailSerializer, FoodCategoryDetailSerializer, \
    FoodDetailSerializer, ActivityDetailSerializer
from apps.common import pagination
from apps.journal.models import FoodJournal, ActivityJournal
from apps.journal.serializers import FoodJournalDetailSerializer, ActivityJournalDetailSerializer
from apps.search import filtersets


class SearchBaseViewSet(ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    model = None
    serializer_class = None
    filterset_class = None

    def get_queryset(self):
        query = Q(is_public=True) | Q(user=self.request.user.id)
        return self.model.objects.filter(query)


class SearchFoodPortionViewSet(SearchBaseViewSet):
    """ Search in food portions. Queryset: user=request.user or is public=True"""
    model = FoodPortion
    serializer_class = FoodPortionDetailSerializer
    filterset_class = filtersets.FoodPortionFilterSet


class SearchFoodCategoryViewSet(SearchBaseViewSet):
    """ Search in food categories. Queryset: user=request.user or is public=True"""
    model = FoodCategory
    serializer_class = FoodCategoryDetailSerializer
    filterset_class = filtersets.FoodCategoryFilterSet


class SearchFoodViewSet(SearchBaseViewSet):
    """ Search in foods. Paginated. Queryset: user=request.user or is public=True"""
    model = Food
    serializer_class = FoodDetailSerializer
    filterset_class = filtersets.FoodFilterSet
    pagination_class = pagination.StandardPagination


class SearchActivityViewSet(SearchBaseViewSet):
    """ Search in activities. Paginated. Queryset: user=request.user or is public=True"""
    model = Activity
    serializer_class = ActivityDetailSerializer
    filterset_class = filtersets.ActivityFilterSet
    pagination_class = pagination.StandardPagination


class SearchFoodJournalViewSet(SearchBaseViewSet):
    """ Search in food journal. Queryset: user=request.user """
    model = FoodJournal
    serializer_class = FoodJournalDetailSerializer
    filterset_class = filtersets.FoodJournalFilterSet

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user.id)


class SearchActivityJournalViewSet(SearchBaseViewSet):
    """ Search in activity journal. Queryset: user=request.user """
    model = ActivityJournal
    serializer_class = ActivityJournalDetailSerializer
    filterset_class = filtersets.ActivityJournalFilterSet

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user.id)
