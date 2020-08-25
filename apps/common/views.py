from abc import ABC

from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)

from apps.common.permissions import IsOwner, HasAPIKey


class BaseViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin,
                  UpdateModelMixin, DestroyModelMixin, GenericViewSet, ABC):
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
        return self.model.objects.filter(user=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(is_public=False, user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(is_public=False, user=self.request.user)


class SearchBaseViewSet(ListModelMixin, GenericViewSet, ABC):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    model = None
    serializer_class = None
    filterset_class = None

    def get_queryset(self):
        query = Q(is_public=True) | Q(user=self.request.user.id)
        return self.model.objects.filter(query)
