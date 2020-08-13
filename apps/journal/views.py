from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.common.permissions import IsOwner
from apps.journal import models
from apps.journal import serializers


class FoodPortionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return serializers.FoodPortionDetailSerializer

        if self.action in ('create', 'update', 'partial_update'):
            return serializers.FoodPortionCreateSerializer

    def get_queryset(self):
        return models.FoodPortion.objects.filter(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        instance = serializer(data=request.data)

        if not instance.is_valid():
            return Response(instance.errors)

        instance.save(is_public=False, owner=request.user)
        return Response(instance.data)


class FoodCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return serializers.FoodCategoryDetailSerializer

        if self.action in ('create', 'update', 'partial_update'):
            return serializers.FoodCategoryCreateSerializer

    def get_queryset(self):
        return models.FoodCategory.objects.filter(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        instance = serializer(data=request.data)

        if not instance.is_valid():
            return Response(instance.errors)

        instance.save(is_public=False, owner=request.user)
        return Response(instance.data)


class FoodViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return serializers.FoodDetailSerializer

        if self.action in ('create', 'update', 'partial_update'):
            return serializers.FoodCreateSerializer

    def get_queryset(self):
        return models.Food.objects.filter(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        instance = serializer(data=request.data)

        if not instance.is_valid():
            return Response(instance.errors)

        instance.save(is_public=False, owner=request.user)
        return Response(instance.data)


class ActivityCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return serializers.ActivityCategoryDetailSerializer

        if self.action in ('create', 'update', 'partial_update'):
            return serializers.ActivityCategoryCreateSerializer

    def get_queryset(self):
        return models.ActivityCategory.objects.filter(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        instance = serializer(data=request.data)

        if not instance.is_valid():
            return Response(instance.errors)

        instance.save(is_public=False, owner=request.user)
        return Response(instance.data)


class ActivityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return serializers.ActivityDetailSerializer

        if self.action in ('create', 'update', 'partial_update'):
            return serializers.ActivityCreateSerializer

    def get_queryset(self):
        return models.Activity.objects.filter(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        instance = serializer(data=request.data)

        if not instance.is_valid():
            return Response(instance.errors)

        instance.save(is_public=False, owner=request.user)
        return Response(instance.data)


class FoodJournalViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return serializers.FoodJournalDetailSerializer

        if self.action in ('create', 'update', 'partial_update'):
            return serializers.FoodJournalCreateSerializer

    def get_queryset(self):
        return models.FoodJournal.objects.filter(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        instance = serializer(data=request.data)

        if not instance.is_valid():
            return Response(instance.errors)

        instance.save(is_public=False, owner=request.user)
        return Response(instance.data)


class ActivityJournalViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return serializers.ActivityJournalDetailSerializer

        if self.action in ('create', 'update', 'partial_update'):
            return serializers.ActivityJournalCreateSerializer

    def get_queryset(self):
        return models.ActivityJournal.objects.filter(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        instance = serializer(data=request.data)

        if not instance.is_valid():
            return Response(instance.errors)

        instance.save(is_public=False, owner=request.user)
        return Response(instance.data)
