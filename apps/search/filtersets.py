from django_filters import FilterSet

from apps.calorie_api.models import FoodPortion, FoodCategory, Food, Activity
from apps.journal.models import FoodJournal, ActivityJournal


class FoodPortionFilterSet(FilterSet):
    class Meta:
        model = FoodPortion
        fields = {
            'id': [
                'exact', 'in',
            ],
            'title': [
                'exact', 'contains',
            ],
        }


class FoodCategoryFilterSet(FilterSet):
    class Meta:
        model = FoodCategory
        fields = {
            'id': [
                'exact', 'in',
            ],
            'title': [
                'exact', 'contains',
            ],
        }


class FoodFilterSet(FilterSet):
    class Meta:
        model = Food
        fields = {
            'id': [
                'exact', 'in',
            ],
            'title': [
                'exact', 'contains',
            ],
            'category__id': [
                'exact', 'in',
            ],
            'category__title': [
                'exact', 'contains',
            ],
            'energy': [
                'exact', 'gte', 'lte',
            ],
            'protein': [
                'exact', 'gte', 'lte',
            ],
            'carbohydrate': [
                'exact', 'gte', 'lte',
            ],
            'fat': [
                'exact', 'gte', 'lte',
            ],
            'fiber': [
                'exact', 'gte', 'lte',
            ],
            'sugar': [
                'exact', 'gte', 'lte',
            ],
            'salt': [
                'exact', 'gte', 'lte',
            ],
        }


class ActivityFilterSet(FilterSet):
    class Meta:
        model = Activity
        fields = {
            'id': [
                'exact', 'in',
            ],
            'title': [
                'exact', 'contains',
            ],
            'energy': [
                'exact', 'gte', 'lte',
            ],
        }


class FoodJournalFilterSet(FilterSet):
    class Meta:
        model = FoodJournal
        fields = {
            'datetime': [
                'exact', 'gte', 'lte',
            ],
        }


class ActivityJournalFilterSet(FilterSet):
    class Meta:
        model = ActivityJournal
        fields = {
            'datetime': [
                'exact', 'gte', 'lte',
            ],
        }
