from apps.calorie_api.models import (
    FoodPortion,
    FoodCategory,
    Food,
    Activity
)

from apps.calorie_api.serializers import (
    FoodPortionDetailSerializer,
    FoodCategoryDetailSerializer,
    FoodDetailSerializer,
    ActivityDetailSerializer
)

from apps.search.filtersets import (
    FoodPortionFilterSet,
    FoodCategoryFilterSet,
    FoodFilterSet,
    FoodJournalFilterSet,
    ActivityFilterSet,
    ActivityJournalFilterSet,
)


from apps.journal.models import FoodJournal, ActivityJournal
from apps.journal.serializers import FoodJournalDetailSerializer, ActivityJournalDetailSerializer

from apps.common.views import SearchBaseViewSet
from apps.common.pagination import StandardPagination


class SearchFoodPortionViewSet(SearchBaseViewSet):
    """ Search in food portions. Queryset: user=request.user or is public=True"""
    model = FoodPortion
    serializer_class = FoodPortionDetailSerializer
    filterset_class = FoodPortionFilterSet


class SearchFoodCategoryViewSet(SearchBaseViewSet):
    """ Search in food categories. Queryset: user=request.user or is public=True"""
    model = FoodCategory
    serializer_class = FoodCategoryDetailSerializer
    filterset_class = FoodCategoryFilterSet


class SearchFoodViewSet(SearchBaseViewSet):
    """ Search in foods. Paginated. Queryset: user=request.user or is public=True"""
    model = Food
    serializer_class = FoodDetailSerializer
    filterset_class = FoodFilterSet
    pagination_class = StandardPagination


class SearchActivityViewSet(SearchBaseViewSet):
    """ Search in activities. Paginated. Queryset: user=request.user or is public=True"""
    model = Activity
    serializer_class = ActivityDetailSerializer
    filterset_class = ActivityFilterSet
    pagination_class = StandardPagination


class SearchFoodJournalViewSet(SearchBaseViewSet):
    """ Search in food journal. Queryset: user=request.user """
    model = FoodJournal
    serializer_class = FoodJournalDetailSerializer
    filterset_class = FoodJournalFilterSet

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user.id)


class SearchActivityJournalViewSet(SearchBaseViewSet):
    """ Search in activity journal. Queryset: user=request.user """
    model = ActivityJournal
    serializer_class = ActivityJournalDetailSerializer
    filterset_class = ActivityJournalFilterSet

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user.id)
