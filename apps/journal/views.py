from apps.common.views import BaseViewSet
from apps.journal import models, serializers


class FoodJournalViewSet(BaseViewSet):
    """ CRUD on user's FoodJournal. Queryset: user=request.user """
    model = models.FoodJournal
    detail_serializer_class = serializers.FoodJournalDetailSerializer
    create_serializer_class = serializers.FoodJournalCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class ActivityJournalViewSet(BaseViewSet):
    """ CRUD on user's ActivityJournal. Queryset: user=request.user """
    model = models.ActivityJournal
    detail_serializer_class = serializers.ActivityJournalDetailSerializer
    create_serializer_class = serializers.ActivityJournalCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
