from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.common.permissions import IsOwner, HasAPIKey
from apps.journal import models
from apps.journal import serializers


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner, HasAPIKey]
    model = None
    detail_serializer_class = None
    create_serializer_class = None

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return self.detail_serializer_class

        if self.action in ('create', 'update', 'partial_update'):
            return self.create_serializer_class

    def get_queryset(self):
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


class FoodJournalViewSet(BaseViewSet):
    """ CRUD on user's FoodJournal. Queryset: user=request.user """
    model = models.FoodJournal
    detail_serializer_class = serializers.FoodJournalDetailSerializer
    create_serializer_class = serializers.FoodJournalCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ActivityJournalViewSet(BaseViewSet):
    """ CRUD on user's ActivityJournal. Queryset: user=request.user """
    model = models.ActivityJournal
    detail_serializer_class = serializers.ActivityJournalDetailSerializer
    create_serializer_class = serializers.ActivityJournalCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
