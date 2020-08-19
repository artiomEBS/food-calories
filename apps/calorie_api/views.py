from rest_framework import viewsets
from rest_framework.response import Response

from apps.common.permissions import IsOwner, HasAPIKey
from apps.calorie_api import models
from apps.calorie_api import serializers
from rest_framework.permissions import IsAuthenticated


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, HasAPIKey, IsOwner]
    model = None
    detail_serializer_class = None
    create_serializer_class = None

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return self.detail_serializer_class

        if self.action in ('create', 'update', 'partial_update'):
            return self.create_serializer_class

    def get_queryset(self):
        # Fixture for swagger schema generation error
        # TypeError: Field 'id' expected a number but got <django.contrib.auth.models.AnonymousUser object.
        if self.request.user.id is None:
            return self.model.objects.none()

        return self.model.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        self.perform_create(serializer)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(is_public=False, user=self.request.user)

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
