from rest_framework.serializers import Serializer, IntegerField, FloatField


class StatusSerializer(Serializer):
    today_energy = FloatField()
    today_protein = FloatField()
    today_carbohydrate = FloatField()
    today_fat = FloatField()
    today_fiber = FloatField()
    today_sugar = FloatField()
    today_salt = FloatField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
