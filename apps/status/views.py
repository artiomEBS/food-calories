from datetime import date
from apps.status.serializers import StatusSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.journal import models
from apps.journal.models import FoodJournal, ActivityJournal
from apps.users.models import Profile




class StatusView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StatusSerializer

    def get(self, request):
        user_profile = Profile.objects.filter(user=request.user).first()
        user_weight = Profile.weight

        food_journal_queryset = FoodJournal.objects.filter(user=request.user, datetime__date=date.today())
        activity_journal_queryset = ActivityJournal.objects.filter(user=request.user, datetime__date=date.today())

        energy_today = 0
        protein_today = 0
        carbohydrate_today = 0
        fat_today = 0
        fiber_today = 0
        sugar_today = 0
        salt_today = 0
        energy_use = 0

        for food_journal in food_journal_queryset:
            energy_today += food_journal.food.energy * food_journal.weight
            protein_today += food_journal.food.protein * food_journal.weight
            carbohydrate_today = food_journal.food.carbohydrate * food_journal.weight
            fat_today = food_journal.food.fat * food_journal.weight
            fiber_today = food_journal.food.fiber * food_journal.weight
            sugar_today = food_journal.food.sugar * food_journal.weight
            salt_today = food_journal.food.salt * food_journal.weight

        for activity_journal in activity_journal_queryset:
            energy_use += activity_journal.duration * Profile.weight * energy_today

        energy_use = energy_today - energy_use

        serializer = StatusSerializer(data=dict(
            energy_today=energy_today,
            protein_today=protein_today,
            carbohydrate_today=carbohydrate_today,
            fat_today=fat_today,
            fiber_today=fiber_today,
            sugar_today=sugar_today,
            salt_today=salt_today,
        ))

        if not serializer.is_valid():
            return Response(serializer.errors)

        return Response(serializer.data)




        # for activity_journal in activity_journal_queryset:
        #     energy_userd += activity_journal.activity.energy * activity_journal.duation * user.profile.weight
        #
        # energy_today = energy_today - energy_userd
        #
        #
        # result = StatusSerializer(
        #     energy_today=energy_today,
        #     protein_today=protein_today,
        #
        # )
        #
        # return Response(result)
