from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from apps.journal.serializers import (
    FoodJournalCreateSerializer,
    FoodJournalDetailSerializer,
    ActivityJournalCreateSerializer,
    ActivityJournalDetailSerializer,
)
from apps.journal.models import FoodJournal, ActivityJournal


# class DiaryFoodPostView(APIView):
#     permission_classes = [IsAuthenticated]
#     operation_post = ""
#
#     @swagger_auto_schema(request_body=FoodJournalCreateSerializer, operation_description=operation_post)
#     def post(self, request):
#         serializer = FoodJournalCreateSerializer(data=request.data)
#
#         if not serializer.is_valid():
#             raise ValidationError(serializer.errors)
#
#         food = FoodJournal.objects.create(
#             user_id=request.user.id,
#             **serializer.validated_data
#         )
#
#         return Response(FoodJournalDetailSerializer(food).data)

class DiaryFoodView(APIView):
    permission_classes = [IsAuthenticated]
    operation_post = "It create diary food"

    @swagger_auto_schema(request_body=FoodJournalCreateSerializer, operation_description=operation_post)
    def post(self, request):
        serializer = FoodJournalCreateSerializer(data=request.data)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        food = FoodJournal.objects.create(
            user_id=request.user.id,
            **serializer.validated_data
        )

        return Response(FoodJournalDetailSerializer(food).data)

    def patch(self, request):
        """ Update diary food """

    def delete(self, request):
        """ Delete diary food """


class DiaryActivityView(APIView):
    permission_classes = [IsAuthenticated]

    operation_post = "It create diary activity"
    operation_patch = ""
    operation_delete = ""

    @swagger_auto_schema(request_body=ActivityJournalCreateSerializer, operation_description=operation_post)
    def post(self, request):
        serializer = ActivityJournalCreateSerializer(data=request.data)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        activity = ActivityJournal.objects.create(
            user_id=request.user.id,
            **serializer.validated_data
        )

        return Response(ActivityJournalDetailSerializer(activity).data)

    @swagger_auto_schema(request_body=ActivityJournalCreateSerializer, operation_description=operation_patch)
    def patch(self, request, pk):
        serializer = ActivityJournalCreateSerializer(data=request.data)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        activity = ActivityJournal.objects.u(
            user_id=request.user.id,
            **serializer.validated_data
        )

        return Response(ActivityJournalDetailSerializer(activity).data)

    @swagger_auto_schema(operation_description=operation_delete)
    def delete(self, request, pk):
        pass
