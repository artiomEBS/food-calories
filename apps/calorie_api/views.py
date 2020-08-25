from apps.common.views import BaseViewSet
from apps.calorie_api import models, serializers


class FoodPortionViewSet(BaseViewSet):
    """ CRUD on user's FoodPortions. Queryset: user=request.user """
    model = models.FoodPortion
    detail_serializer_class = serializers.FoodPortionDetailSerializer
    create_serializer_class = serializers.FoodPortionCreateSerializer


class FoodCategoryViewSet(BaseViewSet):
    """ CRUD on user's FoodCategories. Queryset: user=request.user """
    model = models.FoodCategory
    detail_serializer_class = serializers.FoodCategoryDetailSerializer
    create_serializer_class = serializers.FoodCategoryCreateSerializer


class FoodViewSet(BaseViewSet):
    """ CRUD on user's Foods. Queryset: user=request.user """
    model = models.Food
    detail_serializer_class = serializers.FoodDetailSerializer
    create_serializer_class = serializers.FoodCreateSerializer


class ActivityViewSet(BaseViewSet):
    """ CRUD on user's Activities. Queryset: user=request.user """
    model = models.Activity
    detail_serializer_class = serializers.ActivityDetailSerializer
    create_serializer_class = serializers.ActivityCreateSerializer
