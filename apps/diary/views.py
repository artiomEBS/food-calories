from datetime import date
from apps.journal.models import FoodJournal, ActivityJournal
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from apps.status.serializers import StatusSerializer
from apps.users.models import Profile
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from apps.journal.serializers import (
    FoodJournalCreateSerializer,
    FoodJournalDetailSerializer,
    ActivityJournalCreateSerializer,
    ActivityJournalDetailSerializer,
)


class DiaryStatusDetailView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StatusSerializer

    def get(self, request):
        # noqa - cautam in jurnal tot ce a mincat azi userul
        food_journal_list_today = FoodJournal.objects.filter(
            user=self.request.user.id,
            datetime__date=date.today(),
        )

        # noqa - Calculam suma totala a nutrientilor consumati stazi
        today_energy = 0
        today_protein = 0
        today_carbohydrate = 0
        today_fat = 0
        today_fiber = 0
        today_sugar = 0
        today_salt = 0
        for food_journal in food_journal_list_today:
            today_energy += food_journal.food.energy * food_journal.weight
            today_protein += food_journal.food.protein * food_journal.weight
            today_carbohydrate += food_journal.food.carbohydrate * food_journal.weight
            today_fat += food_journal.food.fat * food_journal.weight
            today_fiber += food_journal.food.fiber * food_journal.weight
            today_sugar += food_journal.food.sugar * food_journal.weight
            today_salt += food_journal.food.salt * food_journal.weight


        # noqa - Cautam profilul utilizatorului pentru a scoate din el greutatea utilizatorului
        user_profile = Profile.objects.filter(user=self.request.user.id).first()

        if user_profile is None:
            return Response("User doesn't have a profile", status=404)

        if user_profile.weight is None:
            return Response("User doesn't have completed profile")

        # noqa - Cautam toate activitatile pe care utilizatorul lea facut astazi
        activity_journal_list_today = ActivityJournal.objects.filter(
            user=self.request.user.id,
            datetime__date=date.today(),
        )

        # noqa - Calculam energia totala cheltuita astazi
        today_energy_used = 0
        for activity_journal in activity_journal_list_today:
            today_energy_used += activity_journal.activity.energy * activity_journal.duration * user_profile.weight

        # noqa - Scadem energia cheltuita din energia consumata
        today_energy -= today_energy_used

        print('today_energy: ', today_energy)

        # noqa - Gatim raspunsul
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=dict(
            today_energy=today_energy,
            today_protein=today_protein,
            today_carbohydrate=today_carbohydrate,
            today_fat=today_fat,
            today_fiber=today_fiber,
            today_sugar=today_sugar,
            today_salt=today_salt,
        ))

        if not serializer.is_valid():
            return Response(serializer.errors)

        return Response(serializer.validated_data)


class DiaryActivityCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=ActivityJournalCreateSerializer)
    def post(self, request):
        serializer = ActivityJournalCreateSerializer(data=request.data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        activity = ActivityJournal.objects.create(user_id=request.user.id, **serializer.validated_data)
        return Response(ActivityJournalDetailSerializer(activity).data)


class DiaryActivityDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=ActivityJournalCreateSerializer)
    def patch(self, request, pk):
        instance = ActivityJournal.objects.get(id=pk)
        serializer = ActivityJournalCreateSerializer(instance, data=request.data, partial=True)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        serializer.save()
        return Response(ActivityJournalDetailSerializer(instance).data)

    def delete(self, request, pk):
        instance = ActivityJournal.objects.get(id=pk)
        instance.delete()
        return Response('')


class DiaryFoodCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=FoodJournalCreateSerializer)
    def post(self, request):
        serializer = FoodJournalCreateSerializer(data=request.data)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        food = FoodJournal.objects.create(
            user_id=request.user.id,
            **serializer.validated_data
        )

        return Response(FoodJournalDetailSerializer(food).data)


class DiaryFoodDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=FoodJournalCreateSerializer)
    def patch(self, request, pk):

        instance = FoodJournal.objects.get(id=pk)
        serializer = FoodJournalCreateSerializer(instance, data=request.data, partial=True)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        serializer.save()

        return Response(FoodJournalDetailSerializer(instance).data)

    def delete(self, request, pk):
        instance = FoodJournal.objects.get(id=pk)
        instance.delete()
        return Response('')
