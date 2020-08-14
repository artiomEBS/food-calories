from django_filters import FilterSet
from apps.journal import models


class FoodPortionFilterSet(FilterSet):
    class Meta:
        model = models.FoodPortion
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
        model = models.FoodCategory
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
        model = models.Food
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


class ActivityCategoryFilterSet(FilterSet):
    class Meta:
        model = models.ActivityCategory
        fields = {
            'id': [
                'exact', 'in',
            ],
            'title': [
                'exact', 'contains',
            ],
        }


class ActivityFilterSet(FilterSet):
    class Meta:
        model = models.Activity
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
        }


class FoodJournalFilterSet(FilterSet):
    class Meta:
        model = models.FoodJournal
        fields = {
            'datetime': [
                'exact', 'gte', 'lte',
            ],
        }


class ActivityJournalFilterSet(FilterSet):
    class Meta:
        model = models.ActivityJournal
        fields = {
            'datetime': [
                'exact', 'gte', 'lte',
            ],
        }
