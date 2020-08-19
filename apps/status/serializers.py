from rest_framework.serializers import Serializer, IntegerField, FloatField


class StatusSerializer(Serializer):
    energy_today = IntegerField()
    protein_today = FloatField()
    carbohydrate_today = FloatField()
    fat_today = FloatField()
    fiber_today = FloatField()
    sugar_today = FloatField()
    salt_today = FloatField()
